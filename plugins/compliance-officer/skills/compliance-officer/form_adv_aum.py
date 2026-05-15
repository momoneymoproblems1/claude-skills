#!/usr/bin/env python3
"""
Form ADV Regulatory AUM Calculator - SEC Rule 203-1

Calculates regulatory assets under management (RAUM) for Form ADV Part 1A
Item 5.F following SEC guidance and interpretations.

This is NOT the same as total client assets. SEC has specific rules for what
counts as "regulatory AUM" for registration threshold purposes.

Usage:
    python form_adv_aum.py \\
        --discretionary-accounts 85000000 \\
        --non-discretionary-accounts 15000000 \\
        --model-delivery-accounts 10000000 \\
        --consulting-only-accounts 5000000 \\
        --exclude-foreign-clients 2000000 \\
        --output form_adv_aum.json

Reference: SEC Rule 203-1, Form ADV Instructions Part 1A Item 5.F

Author: Financial Services Skills Project
Version: 1.0.0
Last Updated: 2025-01-18
"""

import argparse
import json
import sys
from datetime import datetime
from typing import Dict, Any


class FormADVAUMCalculator:
    """Calculate regulatory AUM for Form ADV per SEC rules."""

    def __init__(self):
        """Initialize calculator with SEC thresholds."""

        # SEC Registration Thresholds (as of 2023, indexed annually)
        self.sec_registration_threshold = 110_000_000  # $110M
        self.mid_sized_adviser_floor = 25_000_000      # $25M
        self.small_adviser_ceiling = 25_000_000        # <$25M (state registered)

        # Buffer zone for registration (advisers between $100M-110M)
        self.buffer_zone_floor = 100_000_000

    def _validate_inputs(
        self,
        discretionary_accounts: float,
        non_discretionary_accounts: float,
        model_delivery_accounts: float,
        consulting_only_accounts: float,
        exclude_foreign_clients: float,
        exclude_proprietary: float,
        exclude_pensions: float,
        exclude_family_offices: float
    ) -> None:
        """Validate all inputs."""

        if discretionary_accounts < 0:
            raise ValueError("Discretionary accounts cannot be negative")

        if non_discretionary_accounts < 0:
            raise ValueError("Non-discretionary accounts cannot be negative")

        if model_delivery_accounts < 0:
            raise ValueError("Model delivery accounts cannot be negative")

        if consulting_only_accounts < 0:
            raise ValueError("Consulting-only accounts cannot be negative")

        if exclude_foreign_clients < 0:
            raise ValueError("Foreign client exclusions cannot be negative")

        if exclude_proprietary < 0:
            raise ValueError("Proprietary exclusions cannot be negative")

        if exclude_pensions < 0:
            raise ValueError("Pension exclusions cannot be negative")

        if exclude_family_offices < 0:
            raise ValueError("Family office exclusions cannot be negative")

    def _calculate_raum_components(
        self,
        discretionary_accounts: float,
        non_discretionary_accounts: float,
        model_delivery_accounts: float,
        consulting_only_accounts: float
    ) -> Dict[str, float]:
        """
        Calculate RAUM components per SEC guidance.

        Key Rules:
        1. Discretionary accounts: COUNT at full value
        2. Non-discretionary accounts: COUNT at full value
        3. Model delivery (non-discretionary): COUNT if have continuous contact
        4. Consulting-only: DO NOT COUNT (no continuous/regular basis)
        """

        # Include discretionary (full value)
        included_discretionary = discretionary_accounts

        # Include non-discretionary (full value)
        included_non_discretionary = non_discretionary_accounts

        # Model delivery: COUNT (meets continuous contact test)
        # Note: Only include if you have continuous/regular contact with client
        # re: their account (even if non-discretionary)
        included_model_delivery = model_delivery_accounts

        # Consulting-only: EXCLUDE (no continuous contact)
        # These are one-time or sporadic advice, not continuous basis
        excluded_consulting = consulting_only_accounts

        # Total includable
        total_includable = (
            included_discretionary +
            included_non_discretionary +
            included_model_delivery
        )

        return {
            "included_discretionary": included_discretionary,
            "included_non_discretionary": included_non_discretionary,
            "included_model_delivery": included_model_delivery,
            "excluded_consulting_only": excluded_consulting,
            "total_includable": total_includable
        }

    def _apply_exclusions(
        self,
        total_includable: float,
        exclude_foreign_clients: float,
        exclude_proprietary: float,
        exclude_pensions: float,
        exclude_family_offices: float
    ) -> Dict[str, float]:
        """
        Apply SEC-permitted exclusions to RAUM.

        Key Exclusions:
        1. Foreign clients (if adviser has no US place of business)
        2. Proprietary assets (assets of the adviser or related persons)
        3. Certain pension consulting assets (ERISA plans you consult to, don't manage)
        4. Family office assets (if registered as family office)
        """

        # Apply exclusions
        total_exclusions = (
            exclude_foreign_clients +
            exclude_proprietary +
            exclude_pensions +
            exclude_family_offices
        )

        # Calculate RAUM
        regulatory_aum = max(0, total_includable - total_exclusions)

        return {
            "total_includable_before_exclusions": total_includable,
            "exclude_foreign_clients": exclude_foreign_clients,
            "exclude_proprietary": exclude_proprietary,
            "exclude_pensions": exclude_pensions,
            "exclude_family_offices": exclude_family_offices,
            "total_exclusions": total_exclusions,
            "regulatory_aum": regulatory_aum
        }

    def _determine_registration_requirement(
        self,
        regulatory_aum: float
    ) -> Dict[str, Any]:
        """
        Determine SEC vs state registration requirement.

        Thresholds:
        - <$25M: Must register with state (unless exempt)
        - $25M-$100M: Mid-sized adviser, generally state-registered
        - $100M-$110M: Buffer zone, can choose SEC or state
        - $110M+: Must register with SEC
        """

        if regulatory_aum >= self.sec_registration_threshold:
            registration_type = "SEC"
            requirement = "Required"
            explanation = (
                f"RAUM of ${regulatory_aum:,.0f} exceeds SEC registration threshold "
                f"(${self.sec_registration_threshold:,.0f}). Must register with SEC."
            )
        elif regulatory_aum >= self.buffer_zone_floor:
            registration_type = "SEC or State (Buffer Zone)"
            requirement = "Optional"
            explanation = (
                f"RAUM of ${regulatory_aum:,.0f} is in buffer zone "
                f"(${self.buffer_zone_floor:,.0f}-${self.sec_registration_threshold:,.0f}). "
                "Adviser may choose SEC or state registration."
            )
        elif regulatory_aum >= self.mid_sized_adviser_floor:
            registration_type = "State"
            requirement = "Required (Mid-Sized)"
            explanation = (
                f"RAUM of ${regulatory_aum:,.0f} is between "
                f"${self.mid_sized_adviser_floor:,.0f} and ${self.buffer_zone_floor:,.0f}. "
                "Adviser must register with state(s) unless exempt."
            )
        else:
            registration_type = "State"
            requirement = "Required (Small)"
            explanation = (
                f"RAUM of ${regulatory_aum:,.0f} is below ${self.mid_sized_adviser_floor:,.0f}. "
                "Adviser must register with state(s) unless exempt."
            )

        # Form ADV reporting bracket
        # Item 5.F uses specific brackets
        if regulatory_aum == 0:
            reporting_bracket = "$0"
        elif regulatory_aum < 10_000_000:
            reporting_bracket = "$0 - $10M"
        elif regulatory_aum < 25_000_000:
            reporting_bracket = "$10M - $25M"
        elif regulatory_aum < 50_000_000:
            reporting_bracket = "$25M - $50M"
        elif regulatory_aum < 100_000_000:
            reporting_bracket = "$50M - $100M"
        elif regulatory_aum < 150_000_000:
            reporting_bracket = "$100M - $150M"
        elif regulatory_aum < 500_000_000:
            reporting_bracket = "$150M - $500M"
        elif regulatory_aum < 1_000_000_000:
            reporting_bracket = "$500M - $1B"
        elif regulatory_aum < 5_000_000_000:
            reporting_bracket = "$1B - $5B"
        elif regulatory_aum < 10_000_000_000:
            reporting_bracket = "$5B - $10B"
        elif regulatory_aum < 25_000_000_000:
            reporting_bracket = "$10B - $25B"
        elif regulatory_aum < 50_000_000_000:
            reporting_bracket = "$25B - $50B"
        else:
            reporting_bracket = "$50B+"

        return {
            "registration_type": registration_type,
            "requirement": requirement,
            "explanation": explanation,
            "form_adv_reporting_bracket": reporting_bracket,
            "sec_threshold": self.sec_registration_threshold,
            "buffer_zone_floor": self.buffer_zone_floor,
            "mid_sized_floor": self.mid_sized_adviser_floor
        }

    def _generate_warnings(
        self,
        regulatory_aum: float,
        total_assets: float
    ) -> list:
        """Generate warnings based on RAUM calculation."""

        warnings = []

        # Approaching SEC threshold
        if 95_000_000 <= regulatory_aum < self.sec_registration_threshold:
            gap = self.sec_registration_threshold - regulatory_aum
            warnings.append(
                f"Approaching SEC registration threshold. Only ${gap:,.0f} below $110M. "
                "Plan for SEC registration within 90 days if threshold crossed."
            )

        # In buffer zone
        if self.buffer_zone_floor <= regulatory_aum < self.sec_registration_threshold:
            warnings.append(
                "In buffer zone ($100M-$110M). May voluntarily register with SEC to avoid "
                "switching if grow past $110M."
            )

        # Large difference between total assets and RAUM
        if total_assets > 0:
            difference_percentage = abs(total_assets - regulatory_aum) / total_assets
            if difference_percentage > 0.20:
                warnings.append(
                    f"Large difference between total client assets (${total_assets:,.0f}) "
                    f"and regulatory AUM (${regulatory_aum:,.0f}). Verify exclusions are correct."
                )

        # Very small RAUM
        if regulatory_aum < 1_000_000 and regulatory_aum > 0:
            warnings.append(
                "Very low regulatory AUM (<$1M). Verify all includable assets are captured. "
                "Most state-registered advisers have minimum capital or bond requirements."
            )

        return warnings

    def calculate_form_adv_aum(
        self,
        discretionary_accounts: float,
        non_discretionary_accounts: float = 0,
        model_delivery_accounts: float = 0,
        consulting_only_accounts: float = 0,
        exclude_foreign_clients: float = 0,
        exclude_proprietary: float = 0,
        exclude_pensions: float = 0,
        exclude_family_offices: float = 0
    ) -> Dict[str, Any]:
        """
        Calculate Form ADV regulatory AUM following SEC guidance.

        Returns dict with calculation breakdown, registration determination, and warnings.
        """

        # Validate inputs
        self._validate_inputs(
            discretionary_accounts, non_discretionary_accounts,
            model_delivery_accounts, consulting_only_accounts,
            exclude_foreign_clients, exclude_proprietary,
            exclude_pensions, exclude_family_offices
        )

        # Calculate components
        components = self._calculate_raum_components(
            discretionary_accounts,
            non_discretionary_accounts,
            model_delivery_accounts,
            consulting_only_accounts
        )

        # Apply exclusions
        exclusions = self._apply_exclusions(
            components["total_includable"],
            exclude_foreign_clients,
            exclude_proprietary,
            exclude_pensions,
            exclude_family_offices
        )

        # Determine registration requirement
        registration = self._determine_registration_requirement(
            exclusions["regulatory_aum"]
        )

        # Calculate total client assets (for comparison)
        total_client_assets = (
            discretionary_accounts +
            non_discretionary_accounts +
            model_delivery_accounts +
            consulting_only_accounts
        )

        # Generate warnings
        warnings = self._generate_warnings(
            exclusions["regulatory_aum"],
            total_client_assets
        )

        # Compile results
        result = {
            "calculation_date": datetime.now().isoformat(),
            "inputs": {
                "discretionary_accounts": float(discretionary_accounts),
                "non_discretionary_accounts": float(non_discretionary_accounts),
                "model_delivery_accounts": float(model_delivery_accounts),
                "consulting_only_accounts": float(consulting_only_accounts),
                "exclude_foreign_clients": float(exclude_foreign_clients),
                "exclude_proprietary": float(exclude_proprietary),
                "exclude_pensions": float(exclude_pensions),
                "exclude_family_offices": float(exclude_family_offices)
            },
            "step_1_calculate_components": {
                "description": "Determine which assets count as RAUM",
                "included_discretionary": round(components["included_discretionary"], 2),
                "included_non_discretionary": round(components["included_non_discretionary"], 2),
                "included_model_delivery": round(components["included_model_delivery"], 2),
                "excluded_consulting_only": round(components["excluded_consulting_only"], 2),
                "subtotal_includable": round(components["total_includable"], 2),
                "explanation": {
                    "discretionary": "Full value - you have investment discretion",
                    "non_discretionary": "Full value - continuous contact with client",
                    "model_delivery": "Included if continuous/regular contact",
                    "consulting_only": "Excluded - no continuous basis"
                }
            },
            "step_2_apply_exclusions": {
                "description": "Apply SEC-permitted exclusions",
                "subtotal_before_exclusions": round(exclusions["total_includable_before_exclusions"], 2),
                "exclude_foreign_clients": round(exclusions["exclude_foreign_clients"], 2),
                "exclude_proprietary": round(exclusions["exclude_proprietary"], 2),
                "exclude_pensions": round(exclusions["exclude_pensions"], 2),
                "exclude_family_offices": round(exclusions["exclude_family_offices"], 2),
                "total_exclusions": round(exclusions["total_exclusions"], 2),
                "explanation": {
                    "foreign": "Foreign clients if no US place of business",
                    "proprietary": "Adviser or related person assets",
                    "pensions": "ERISA plan consulting (not management)",
                    "family_offices": "If registered as family office"
                }
            },
            "regulatory_aum": round(exclusions["regulatory_aum"], 2),
            "registration_determination": registration,
            "comparison": {
                "total_client_assets": round(total_client_assets, 2),
                "regulatory_aum": round(exclusions["regulatory_aum"], 2),
                "difference": round(total_client_assets - exclusions["regulatory_aum"], 2),
                "note": "Regulatory AUM is often less than total client assets due to exclusions"
            },
            "warnings": warnings,
            "form_adv_reporting": {
                "item_5f_bracket": registration["form_adv_reporting_bracket"],
                "instruction": "Report this bracket in Form ADV Part 1A, Item 5.F",
                "annual_update_required": "Within 90 days of fiscal year-end"
            },
            "next_steps": self._generate_next_steps(
                exclusions["regulatory_aum"],
                registration["registration_type"]
            )
        }

        return result

    def _generate_next_steps(
        self,
        regulatory_aum: float,
        registration_type: str
    ) -> list:
        """Generate actionable next steps."""

        next_steps = []

        if "SEC" in registration_type and "Buffer" not in registration_type:
            next_steps.append(
                "Register with SEC using Form ADV via IARD system (iard.finra.org)"
            )
            next_steps.append(
                "Designate Chief Compliance Officer (CCO) in Form ADV Part 1A, Item 1.L"
            )
            next_steps.append(
                "Prepare Form ADV Part 2A (Brochure) and 2B (Brochure Supplement)"
            )
            next_steps.append(
                "Implement required compliance program per Rule 206(4)-7"
            )
        elif "State" in registration_type:
            next_steps.append(
                "Register with appropriate state securities administrator(s)"
            )
            next_steps.append(
                "Complete state-required exams (Series 65 or Series 66 + Series 7)"
            )
            next_steps.append(
                "Check state requirements for minimum net worth or surety bond"
            )
        else:  # Buffer zone
            next_steps.append(
                "Decide whether to register with SEC (optional) or remain state-registered"
            )
            next_steps.append(
                "Consider registering with SEC if expect growth past $110M to avoid switching"
            )

        next_steps.append(
            "Update Form ADV annually within 90 days of fiscal year-end"
        )
        next_steps.append(
            "Monitor AUM quarterly to ensure compliance with registration thresholds"
        )

        return next_steps


def main():
    """Command-line interface for Form ADV AUM calculator."""

    parser = argparse.ArgumentParser(
        description="Calculate regulatory AUM for Form ADV per SEC Rule 203-1"
    )

    # Includable accounts
    parser.add_argument("--discretionary-accounts", type=float, required=True,
                       help="Accounts with investment discretion")
    parser.add_argument("--non-discretionary-accounts", type=float, default=0,
                       help="Non-discretionary accounts with continuous contact")
    parser.add_argument("--model-delivery-accounts", type=float, default=0,
                       help="Model delivery accounts (non-discretionary, continuous contact)")
    parser.add_argument("--consulting-only-accounts", type=float, default=0,
                       help="Consulting-only accounts (excluded from RAUM)")

    # Exclusions
    parser.add_argument("--exclude-foreign-clients", type=float, default=0,
                       help="Foreign client assets (if no US place of business)")
    parser.add_argument("--exclude-proprietary", type=float, default=0,
                       help="Proprietary assets (adviser/related persons)")
    parser.add_argument("--exclude-pensions", type=float, default=0,
                       help="ERISA plan consulting assets (not management)")
    parser.add_argument("--exclude-family-offices", type=float, default=0,
                       help="Family office assets")

    # Output
    parser.add_argument("--output", type=str, default="form_adv_aum.json",
                       help="Output JSON file path")

    args = parser.parse_args()

    # Create calculator
    calc = FormADVAUMCalculator()

    try:
        # Calculate
        result = calc.calculate_form_adv_aum(
            discretionary_accounts=args.discretionary_accounts,
            non_discretionary_accounts=args.non_discretionary_accounts,
            model_delivery_accounts=args.model_delivery_accounts,
            consulting_only_accounts=args.consulting_only_accounts,
            exclude_foreign_clients=args.exclude_foreign_clients,
            exclude_proprietary=args.exclude_proprietary,
            exclude_pensions=args.exclude_pensions,
            exclude_family_offices=args.exclude_family_offices
        )

        # Write output
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)

        print(f"Form ADV AUM calculation complete. Results written to {args.output}")
        print(f"\n{'='*60}")
        print(f"REGULATORY AUM (RAUM): ${result['regulatory_aum']:,.0f}")
        print(f"{'='*60}")
        print(f"\nRegistration Type: {result['registration_determination']['registration_type']}")
        print(f"Requirement: {result['registration_determination']['requirement']}")
        print(f"Form ADV Bracket: {result['registration_determination']['form_adv_reporting_bracket']}")
        print(f"\n{result['registration_determination']['explanation']}")

        if result['warnings']:
            print(f"\n⚠ Warnings: {len(result['warnings'])}")
            for warning in result['warnings']:
                print(f"  - {warning}")

        print(f"\nNext Steps:")
        for step in result['next_steps']:
            print(f"  • {step}")

        return 0

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

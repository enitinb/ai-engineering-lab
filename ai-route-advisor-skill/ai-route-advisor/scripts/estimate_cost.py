#!/usr/bin/env python3
"""Simple vendor-neutral cost estimator for comparing route economics.

This does not include any model pricing. Pass your own assumed prices.
"""
import argparse


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-tokens", type=float, required=True)
    parser.add_argument("--output-tokens", type=float, required=True)
    parser.add_argument("--requests", type=float, default=1)
    parser.add_argument("--input-price-per-million", type=float, required=True)
    parser.add_argument("--output-price-per-million", type=float, required=True)
    parser.add_argument("--retry-rate", type=float, default=0.0, help="Expected retry rate, e.g. 0.1 for 10%")
    args = parser.parse_args()

    multiplier = 1 + args.retry_rate
    input_cost = args.requests * args.input_tokens / 1_000_000 * args.input_price_per_million * multiplier
    output_cost = args.requests * args.output_tokens / 1_000_000 * args.output_price_per_million * multiplier
    total = input_cost + output_cost
    print(f"Estimated cost: ${total:.6f}")
    print(f"Input cost:     ${input_cost:.6f}")
    print(f"Output cost:    ${output_cost:.6f}")
    print(f"Retry factor:   {multiplier:.2f}x")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

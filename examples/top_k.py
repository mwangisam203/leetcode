"""Inspect Top K counts and buckets without changing your scratch file."""
import argparse
from collections import Counter

from Hashing.hashing import top_k_frequent

DEFAULT_NUMS = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('nums', type=int, nargs='*', default=DEFAULT_NUMS,
                        help='integers to count; defaults to a ten-number example')
    parser.add_argument('-k', type=int, default=2,
                        help='number of distinct values to return (default: 2)')
    args = parser.parse_args(argv)
    try:
        result = top_k_frequent(args.nums, args.k)
    except ValueError as error:
        parser.error(str(error))

    counts = Counter(args.nums)
    print(f'nums: {args.nums}')
    print(f'length: {len(args.nums)}; distinct: {len(counts)}; k: {args.k}')
    print(f'counts (number -> frequency): {dict(counts)}')
    buckets = {}
    for number, frequency in counts.items():
        buckets.setdefault(frequency, []).append(number)
    for frequency in sorted(buckets, reverse=True):
        print(f'bucket[{frequency}]: {buckets[frequency]}')
    print(f'top {args.k}: {result}')


if __name__ == '__main__':
    main()

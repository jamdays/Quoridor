import sys
from scipy.stats import binom

def calculate_p_value():
    """
    Reads data from standard input, parses total entries, 0s, and 1s counts,
    and calculates the two-tailed p-value for a binomial distribution
    with a null hypothesis probability of 0.5 (50/50 chance).
    """
    lines = sys.stdin.readlines()
    total_entries = 0
    zeros_count = 0
    ones_count = 0

    # Parse the input lines to extract the necessary information
    for line in lines:
        line = line.strip()
        if "Total valid entries:" in line:
            try:
                total_entries = int(line.split(":")[1].strip())
            except ValueError:
                print("Error: Could not parse 'Total valid entries'. Ensure it's an integer.")
                return
        elif "0s:" in line:
            try:
                zeros_count = int(line.split(":")[1].split(" ")[1].strip())
            except ValueError:
                print("Error: Could not parse '0s' count. Ensure it's an integer.")
                return
        elif "1s:" in line:
            try:
                ones_count = int(line.split(":")[1].split(" ")[1].strip())
            except ValueError:
                print("Error: Could not parse '1s' count. Ensure it's an integer.")
                return

    # Validate parsed data
    if total_entries == 0:
        print("Error: 'Total valid entries' is zero or not found. Cannot perform calculation.")
        return
    if (zeros_count + ones_count) != total_entries:
        print("Warning: Sum of 0s and 1s does not match total valid entries.")
        # Continue with calculation using the provided counts, but this indicates potential input discrepancy.

    # Define the parameters for the binomial distribution
    n = total_entries  # Number of trials
    p_null = 0.5       # Null hypothesis probability of success (getting a '1')

    # For a two-tailed binomial test with p_null = 0.5, the distribution is symmetric.
    # We want to find the probability of observing a result as extreme or more extreme
    # than the observed counts (24 '1s' and 26 '0s' in your example).
    # The expected number of 1s (or 0s) is n * p_null = 50 * 0.5 = 25.
    # The observed count of 1s is 24, which deviates by 1 from the mean (25 - 24 = 1).
    # The observed count of 0s is 26, which also deviates by 1 from the mean (26 - 25 = 1).

    # We calculate the cumulative probability of the "less extreme" tail
    # (i.e., the probability of getting 'ones_count' or fewer 1s).
    # Since it's a two-tailed test and p_null = 0.5, we double this tail probability.
    # We use the minimum of the two counts (ones_count or zeros_count) to calculate the lower tail.
    # In your example, min(24, 26) = 24.
    k_for_tail = min(ones_count, zeros_count)

    # Calculate the p-value
    # binom.cdf(k, n, p) calculates P(X <= k)
    # For a two-tailed test, we double the probability of the observed tail.
    p_value = 2 * binom.cdf(k_for_tail, n, p_null)

    # Print the results
    print(f"Total valid entries: {total_entries}")
    print(f"0s: {zeros_count}")
    print(f"1s: {ones_count}")
    print(f"Calculated p-value: {p_value:.4f}")

if __name__ == "__main__":
    calculate_p_value()


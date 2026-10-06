import time
import random

# =======================================================
# DO NOT MODIFY THE ALGORITHM IMPLEMENTATIONS
# =======================================================

def find_duplicates_slow(data):
    """An O(n^2) algorithm to find duplicates."""
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                return True
    return False

def find_duplicates_fast(data):
    """An O(n) algorithm to find duplicates."""
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False


# =======================================================
# YOUR TASK: FIX THE BENCHMARKING SCRIPT BELOW
# =======================================================

def make_worst_case_data(n, rng):
    """n unique values in random order -> no duplicates, so neither algorithm
    can exit early and both do their full amount of work."""
    return rng.sample(range(n * 10), n)
 
 
def time_once(func, data):
    """Time a single call, with GC paused so collections don't add noise."""
    gc_was_enabled = gc.isenabled()
    gc.disable()
    try:
        start = time.perf_counter()
        result = func(data)
        elapsed = time.perf_counter() - start
    finally:
        if gc_was_enabled:
            gc.enable()
    return elapsed, result
 
 
def benchmark(func, data, repeats):
    """Run func on the same data several times; return (median, min) seconds."""
    func(data)  # warm-up run, not timed
    times = []
    for _ in range(repeats):
        elapsed, _ = time_once(func, data)
        times.append(elapsed)
    return statistics.median(times), min(times)
 
 
def estimate_exponent(sizes, times):
    """Slope of log(time) vs log(n): ~1 means O(n), ~2 means O(n^2)."""
    xs = [math.log(n) for n in sizes]
    ys = [math.log(t) for t in times]
    x_mean, y_mean = statistics.fmean(xs), statistics.fmean(ys)
    num = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys))
    den = sum((x - x_mean) ** 2 for x in xs)
    return num / den
 
 
def run_benchmark(sizes=(250, 500, 1000, 2000, 4000), repeats=7, seed=42):
    rng = random.Random(seed)  # reproducible inputs
    slow_times, fast_times = [], []
 
    print(f"{'n':>8} | {'slow (s)':>12} | {'fast (s)':>12} | {'speedup':>10}")
    print("-" * 52)
 
    for n in sizes:
        # Data is built OUTSIDE the timed region and shared by both algorithms.
        data = make_worst_case_data(n, rng)
 
        # Sanity check: both must agree (and here, both must say "no duplicates").
        assert find_duplicates_slow(data) == find_duplicates_fast(data) == False
 
        slow_med, _ = benchmark(find_duplicates_slow, data, repeats)
        fast_med, _ = benchmark(find_duplicates_fast, data, repeats)
        slow_times.append(slow_med)
        fast_times.append(fast_med)
 
        print(f"{n:>8} | {slow_med:>12.6f} | {fast_med:>12.6f} | {slow_med / fast_med:>9.1f}x")
 
    print("-" * 52)
    print(f"Estimated scaling exponent (slow): {estimate_exponent(sizes, slow_times):.2f}  (expect ~2)")
    print(f"Estimated scaling exponent (fast): {estimate_exponent(sizes, fast_times):.2f}  (expect ~1)")
 
 
if __name__ == "__main__":
    run_benchmark()

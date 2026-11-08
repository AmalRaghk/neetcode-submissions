from collections import Counter


class Solution:

  def minWindow(self, s: str, t: str) -> str:
    if not s or not t or len(s) < len(t):
      return ""

    target_counts = Counter(t)
    window_counts = {}

    have = 0
    need = len(target_counts)

    res = (-1, -1)
    min_len = float("inf")

    left = 0
    for right, char in enumerate(s):
      window_counts[char] = window_counts.get(char, 0) + 1

      if char in target_counts and window_counts[char] == target_counts[char]:
        have += 1

      while have == need:
        window_size = right - left + 1
        if window_size < min_len:
          min_len = window_size
          res = (left, right)

        left_char = s[left]
        window_counts[left_char] -= 1
        if (
            left_char in target_counts
            and window_counts[left_char] < target_counts[left_char]
        ):
          have -= 1

        left += 1

    l, r = res
    return s[l : r + 1] if min_len != float("inf") else ""
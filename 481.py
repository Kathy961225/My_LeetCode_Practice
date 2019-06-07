def magicalString(self, n: int) -> int:
	S = [1, 2, 2]

	i = 2
	while len(S) < n:
		complement = 2 if S[-1] == 1 else 1
		S.extend([complement] * S[i])
		i += 1

	return S[:n].count(1)
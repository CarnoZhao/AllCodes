
result = [
"""
1 x 1 1 x 1
2 2 2 1 2 2
2 x 2 0 1 x
2 x 2 1 2 2
1 1 1 1 x 1
0 0 0 1 1 1
""",
"""
1 1 0 1 1 1 0 0 1 1 1 0 0 0 0 1 1 1 0
x 1 0 1 x 1 0 0 2 x 2 0 0 0 0 1 x 2 1
1 1 0 2 3 3 1 1 3 x 2 0 0 0 0 1 2 x 1
0 1 1 2 x x 1 2 x 3 1 0 0 0 0 0 1 1 1
0 1 x 2 2 2 1 3 x 3 0 0 0 0 0 0 0 0 0
0 1 1 1 0 0 0 2 x 2 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 2 2 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 x x 1 0 0 0 0 0
0 0 1 1 1 0 1 1 1 0 1 2 2 1 0 0 0 0 0
0 0 1 x 2 1 3 x 2 0 0 0 0 0 0 1 1 1 0
0 0 1 1 2 x 3 x 3 1 1 0 0 0 0 1 x 1 0
0 0 0 0 1 2 3 2 2 x 1 0 0 0 0 1 1 1 0
0 0 0 0 0 1 x 1 1 1 1 0 0 0 0 0 1 1 1
0 0 1 1 2 2 2 1 0 0 0 0 0 0 0 0 1 x 1
0 0 1 x 2 x 2 1 1 0 0 0 0 0 0 0 1 1 1
0 0 1 1 2 1 3 x 3 1 0 0 0 0 0 0 0 1 1
0 0 0 0 0 0 2 x x 1 0 0 0 1 1 1 0 1 x
0 0 0 1 1 1 1 2 2 1 0 0 0 1 x 1 1 2 2
0 0 0 1 x 3 2 1 0 0 0 1 1 2 1 1 1 x 2
0 0 0 1 2 x x 1 0 0 0 1 x 1 0 1 2 3 x
0 0 0 0 1 2 2 1 1 1 1 1 1 1 0 1 x 3 2
0 0 0 0 1 1 1 1 2 x 1 1 1 1 0 2 3 x 2
0 0 0 0 1 x 1 1 x 2 1 1 x 1 0 1 x 3 x
""",
"""
0 0 0 0 0 0 0 0 1 x x 2 1 0 1 x 1 0 1 2 x
0 0 0 0 0 0 0 0 1 2 3 x 1 0 2 2 2 1 2 x 2
0 0 0 0 0 0 0 0 0 0 2 2 2 0 1 x 1 1 x 2 1
0 0 0 0 0 1 1 1 0 0 1 x 1 0 1 2 2 2 1 1 0
1 1 0 0 0 1 x 1 0 1 2 2 1 0 0 1 x 1 1 1 1
x 1 0 0 0 1 1 1 0 1 x 1 0 0 0 1 1 1 1 x 1
2 2 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 1 1 1
1 x 1 0 0 0 0 0 0 0 1 2 2 1 0 0 1 1 1 0 0
1 1 1 0 0 0 0 0 0 0 1 x x 1 0 0 1 x 1 0 0
""",
"""
0 0 0 0 0 0 0 0 0 0 0 0 1 x 1 0 0 0 0 0 0 0 0 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 1 1 1 0 0 0 0 2 x 2 1 x 1 0
1 1 1 0 0 0 0 1 1 1 0 0 0 0 1 1 2 x 1 0 0 0 0 2 x 2 1 1 1 0
1 x 1 1 1 1 0 1 x 2 1 1 0 0 1 x 2 1 1 0 0 0 0 1 1 1 0 0 0 0
1 2 2 3 x 2 0 1 1 2 x 1 0 0 1 2 2 1 0 0 0 0 0 1 1 1 0 0 1 1
0 1 x 3 x 2 0 0 0 1 1 1 0 1 2 3 x 1 0 0 0 0 0 1 x 1 0 0 1 x
0 1 1 3 3 3 2 1 1 1 1 2 1 2 x x 2 2 1 1 0 0 0 1 1 1 1 1 2 1
0 0 0 1 x x 2 x 1 1 x 2 x 2 3 3 3 2 x 1 0 1 1 1 0 0 2 x 2 0
0 1 1 2 2 2 3 2 2 1 1 2 1 1 1 x 2 x 2 1 0 1 x 1 0 0 2 x 2 0
1 2 x 1 0 1 2 x 1 0 0 0 1 1 2 2 3 2 1 0 0 1 1 1 0 0 1 1 1 0
1 x 2 1 0 1 x 3 2 1 0 0 1 x 1 1 x 2 1 0 0 0 1 1 1 0 0 0 0 0
1 1 2 1 2 2 2 2 x 1 0 0 1 1 1 1 2 x 1 0 0 0 1 x 2 1 0 0 0 0
1 1 2 x 2 x 1 1 1 1 0 0 0 0 1 1 2 1 1 0 0 0 1 2 x 1 0 0 0 0
1 x 3 2 2 1 1 0 0 1 1 1 0 0 1 x 1 0 0 0 0 0 1 2 2 1 0 0 0 0
1 2 x 1 0 0 0 0 0 1 x 1 0 0 1 1 1 0 0 0 0 0 1 x 1 0 0 0 0 0
""",
"""
1 x 1 0 1 1 1 0 1 x 2 x 1 0 0 0 1 x 1 0 0 0 0 0 0 1 1 1 0 0
1 1 1 0 1 x 2 2 3 2 2 1 1 0 0 0 1 1 2 1 1 0 0 0 0 1 x 1 0 0
0 0 0 1 2 2 2 x x 2 1 1 0 0 0 0 0 0 1 x 1 0 0 0 0 1 2 2 1 0
1 1 1 1 x 1 1 2 2 2 x 1 1 1 1 0 0 0 1 1 1 0 0 0 0 0 2 x 2 0
2 x 1 1 1 1 1 1 1 1 1 1 1 x 2 1 0 0 0 1 1 1 0 0 0 0 2 x 2 0
x 2 1 0 0 0 1 x 1 0 0 0 2 3 x 1 0 0 0 1 x 1 0 0 0 0 1 1 1 0
1 1 0 0 0 0 2 2 2 0 0 0 1 x 2 1 0 0 0 1 1 1 0 0 0 1 1 1 0 0
0 0 0 0 0 0 1 x 1 0 0 0 2 2 2 0 1 1 1 0 0 0 1 1 1 1 x 1 0 0
0 0 0 0 1 1 2 1 1 0 0 0 1 x 1 0 1 x 1 1 1 2 2 x 1 1 1 1 0 0
0 0 0 0 1 x 1 0 0 0 0 0 1 1 1 0 2 2 2 2 x 3 x 2 1 0 0 0 1 1
0 0 0 0 1 1 1 0 0 0 0 1 1 1 0 0 1 x 1 2 x 4 2 2 0 1 1 1 1 x
0 1 1 1 0 0 0 0 0 0 0 1 x 1 0 0 1 2 2 2 1 2 x 1 0 1 x 1 1 1
0 1 x 2 1 2 1 1 0 0 0 1 1 1 0 0 0 1 x 1 0 1 2 2 1 1 1 1 0 0
0 1 1 2 x 2 x 3 2 1 0 1 2 2 1 0 0 1 2 2 1 0 1 x 1 0 0 0 0 0
1 1 0 1 1 2 2 x x 1 0 1 x x 1 0 0 0 1 x 1 0 1 2 2 1 0 0 0 0
x 1 0 0 0 0 2 3 3 1 0 1 2 2 1 0 0 0 1 1 1 0 0 2 x 2 0 0 0 0
1 1 0 0 0 0 1 x 1 0 0 0 0 1 1 1 0 0 0 0 0 0 0 2 x 3 1 0 0 0
0 0 0 0 0 0 1 1 1 0 0 0 0 1 x 1 0 0 0 1 1 1 0 1 2 x 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 2 x 2 0 1 2 2 1 0 0 0
1 2 2 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 x 2 0 1 x 1 0 1 1 1
1 x x 1 1 1 1 0 1 1 1 0 0 1 1 2 1 1 0 1 1 1 1 2 2 1 0 1 x 1
1 2 3 2 2 x 1 0 1 x 2 1 0 1 x 3 x 2 0 0 0 0 1 x 1 0 0 1 1 1
0 0 1 x 3 2 2 0 1 2 x 1 1 2 2 3 x 3 1 0 0 0 1 1 1 0 0 0 0 0
0 0 1 1 2 x 1 0 0 1 1 2 2 x 2 2 2 x 2 1 1 0 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 0 0 0 0 1 x 4 x 1 1 1 2 x 1 1 1 1 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1 1 2 2 x 2 1 0 0 1 1 1 1 x 2 1 1 0 0 0 0
0 0 0 0 0 1 1 2 1 2 x 1 1 1 1 0 0 1 2 2 1 1 1 2 x 2 1 1 1 1
0 0 0 0 0 1 x 4 x 4 2 1 0 0 0 0 0 2 x x 2 2 2 2 3 x 2 1 x 1
0 0 0 0 0 1 2 x x x 1 0 0 0 0 0 0 2 x 3 2 x x 1 2 x 2 1 1 1
""",
"""
1 x 1 0 0 1 x 2 1 2 x 2 1 1 1 1 2 x 2 1 0 0 0 1 1 1 1 1 1 0
1 1 1 0 0 1 1 3 x 3 1 2 x 1 2 x 3 2 x 1 0 0 0 1 x 1 1 x 1 0
2 2 1 0 1 1 1 2 x 3 1 2 1 1 2 x 2 1 1 1 0 0 0 2 2 2 1 1 1 0
x x 1 0 2 x 2 1 1 3 x 2 1 1 2 1 1 0 0 0 0 0 1 2 x 1 0 0 0 0
2 2 2 1 3 x 2 0 0 3 x 3 1 x 2 1 2 1 1 0 0 0 1 x 2 1 0 0 0 0
0 0 1 x 3 2 1 0 0 2 x 2 1 1 2 x 2 x 1 0 1 2 3 2 1 0 0 0 0 0
0 0 1 2 x 1 0 1 1 2 1 1 0 0 1 1 2 1 2 1 2 x x 1 0 0 0 0 0 0
0 1 1 2 1 1 1 2 x 1 0 0 0 0 0 1 1 1 1 x 2 3 3 2 0 0 0 0 0 0
1 2 x 1 0 0 1 x 3 2 0 0 0 0 0 2 x 3 2 2 1 1 x 2 1 2 1 1 0 0
x 2 1 1 0 0 1 2 x 1 1 1 1 0 0 2 x 3 x 1 0 1 1 2 x 3 x 1 0 0
1 1 0 0 0 0 0 1 1 1 2 x 2 0 0 1 1 3 2 2 0 0 0 1 2 x 2 1 0 0
0 0 0 0 0 0 0 0 0 0 2 x 2 0 0 0 0 1 x 1 0 0 0 1 2 2 1 0 0 0
0 0 0 0 0 0 0 1 1 2 2 2 1 0 0 0 0 1 1 1 0 0 0 1 x 1 0 0 0 0
0 0 0 0 0 0 0 1 x 2 x 1 0 0 0 0 0 0 0 0 0 0 0 1 1 1 0 0 0 0
1 1 0 0 0 0 0 1 1 2 2 2 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1
x 1 0 0 0 0 0 0 0 0 1 x 1 0 0 1 1 1 0 0 1 1 1 1 1 1 0 1 x 2
1 1 0 0 1 1 1 0 0 0 1 1 1 0 0 1 x 1 0 0 1 x 2 2 x 1 0 1 2 x
0 0 0 0 1 x 1 0 1 1 1 0 0 0 0 1 1 1 0 0 2 3 x 3 2 2 0 0 1 1
0 0 0 0 1 1 2 1 2 x 1 1 1 1 0 0 0 0 0 0 1 x 2 2 x 1 0 0 0 0
0 0 0 0 0 0 1 x 2 1 1 1 x 1 0 0 0 0 0 0 1 1 1 2 2 2 1 1 1 0
0 0 0 0 0 0 1 1 2 1 1 1 1 1 0 0 0 0 0 0 0 1 1 2 x 1 1 x 1 0
0 1 1 2 1 1 0 0 1 x 1 0 0 0 0 0 0 1 1 2 1 2 x 2 1 2 3 3 2 0
0 1 x 2 x 1 0 0 1 1 1 0 0 0 0 0 0 1 x 2 x 2 1 1 0 2 x x 1 0
0 1 1 2 1 1 0 0 0 0 0 0 0 0 0 0 0 1 1 2 1 1 0 1 1 3 x 3 1 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 x 3 1 1 0 0
0 1 1 1 0 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 0 0 0 2 x 2 0 1 2 2
1 2 x 1 0 0 0 0 2 x 2 0 0 0 1 x 1 0 0 0 0 1 1 3 2 2 0 1 x x
x 2 1 1 0 0 0 0 3 x 3 0 0 0 1 1 2 1 1 0 0 1 x 2 x 1 1 3 5 4
1 1 0 1 1 1 0 0 2 x 2 0 0 0 0 0 1 x 1 0 0 1 1 2 1 1 2 x x x
0 0 0 1 x 1 0 0 1 1 1 0 0 0 0 0 1 1 1 0 0 0 0 0 0 0 2 x 4 2
""",
"""
1 x 1 0 0 2 x 2 1 x 1 0 0 1 x x 1
1 1 1 0 0 2 x 3 2 1 1 0 0 1 3 4 3
0 0 0 0 0 1 2 x 1 0 0 0 0 0 1 x x
0 0 0 0 0 0 1 1 1 0 0 0 0 0 1 2 2
0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1
1 1 1 0 0 0 0 0 0 0 0 0 0 1 2 x 1
1 x 1 0 0 0 0 0 0 0 0 0 0 1 x 2 1
""",
"""
x x x
x 8 x
x x x
""",
"""
x
"""
]
maps = [
"""
? ? ? ? ? ?
? ? ? ? ? ?
? ? ? 0 ? ?
? ? ? ? ? ?
? ? ? ? ? ?
0 0 0 ? ? ?
""",#6
"""
? ? 0 ? ? ? 0 0 ? ? ? 0 0 0 0 ? ? ? 0
? ? 0 ? ? ? 0 0 ? ? ? 0 0 0 0 ? ? ? ?
? ? 0 ? ? ? ? ? ? ? ? 0 0 0 0 ? ? ? ?
0 ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 ? ? ?
0 ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 0 0
0 ? ? ? 0 0 0 ? ? ? 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 ? ? ? ? ? ? ? 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 ? ? ? ? 0 0 0 0 0
0 0 ? ? ? 0 ? ? ? 0 ? ? ? ? 0 0 0 0 0
0 0 ? ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? 0
0 0 ? ? ? ? ? ? ? ? ? 0 0 0 0 ? ? ? 0
0 0 0 0 ? ? ? ? ? ? ? 0 0 0 0 ? ? ? 0
0 0 0 0 0 ? ? ? ? ? ? 0 0 0 0 0 ? ? ?
0 0 ? ? ? ? ? ? 0 0 0 0 0 0 0 0 ? ? ?
0 0 ? ? ? ? ? ? ? 0 0 0 0 0 0 0 ? ? ?
0 0 ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 ? ?
0 0 0 0 0 0 ? ? ? ? 0 0 0 ? ? ? 0 ? ?
0 0 0 ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? ?
0 0 0 ? ? ? ? ? 0 0 0 ? ? ? ? ? ? ? ?
0 0 0 ? ? ? ? ? 0 0 0 ? ? ? 0 ? ? ? ?
0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ?
0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ?
0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ?
""",#43
"""
0 0 0 0 0 0 0 0 ? ? ? ? ? 0 ? ? ? 0 ? ? ?
0 0 0 0 0 0 0 0 ? ? ? ? ? 0 ? ? ? ? ? ? ?
0 0 0 0 0 0 0 0 0 0 ? ? ? 0 ? ? ? ? ? ? ?
0 0 0 0 0 ? ? ? 0 0 ? ? ? 0 ? ? ? ? ? ? 0
? ? 0 0 0 ? ? ? 0 ? ? ? ? 0 0 ? ? ? ? ? ?
? ? 0 0 0 ? ? ? 0 ? ? ? 0 0 0 ? ? ? ? ? ?
? ? ? 0 0 0 0 0 0 ? ? ? 0 0 0 0 0 0 ? ? ?
? ? ? 0 0 0 0 0 0 0 ? ? ? ? 0 0 ? ? ? 0 0
? ? ? 0 0 0 0 0 0 0 ? ? ? ? 0 0 ? ? ? 0 0
""",
"""
0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 0 0 0 0 0 ? ? ? ? ? ? 0
0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 ? ? ? 0 0 0 0 ? ? ? ? ? ? 0
? ? ? 0 0 0 0 ? ? ? 0 0 0 0 ? ? ? ? ? 0 0 0 0 ? ? ? ? ? ? 0
? ? ? ? ? ? 0 ? ? ? ? ? 0 0 ? ? ? ? ? 0 0 0 0 ? ? ? 0 0 0 0
? ? ? ? ? ? 0 ? ? ? ? ? 0 0 ? ? ? ? 0 0 0 0 0 ? ? ? 0 0 ? ?
0 ? ? ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? ? 0 0 0 0 0 ? ? ? 0 0 ? ?
0 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? ? ?
0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 ? ? ? 0 0 ? ? ? 0
0 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 ? ? ? 0 0 ? ? ? 0
? ? ? ? 0 ? ? ? ? 0 0 0 ? ? ? ? ? ? ? 0 0 ? ? ? 0 0 ? ? ? 0
? ? ? ? 0 ? ? ? ? ? 0 0 ? ? ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 0
? ? ? ? ? ? ? ? ? ? 0 0 ? ? ? ? ? ? ? 0 0 0 ? ? ? ? 0 0 0 0
? ? ? ? ? ? ? ? ? ? 0 0 0 0 ? ? ? ? ? 0 0 0 ? ? ? ? 0 0 0 0
? ? ? ? ? ? ? 0 0 ? ? ? 0 0 ? ? ? 0 0 0 0 0 ? ? ? ? 0 0 0 0
? ? ? ? 0 0 0 0 0 ? ? ? 0 0 ? ? ? 0 0 0 0 0 ? ? ? 0 0 0 0 0
""",#45
"""
? ? ? 0 ? ? ? 0 ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 0 0 ? ? ? 0 0
? ? ? 0 ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? 0 0 0 0 ? ? ? 0 0
0 0 0 ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? 0 0 0 0 ? ? ? ? 0
? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 0 ? ? ? 0
? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0
? ? ? 0 0 0 ? ? ? 0 0 0 ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0
? ? 0 0 0 0 ? ? ? 0 0 0 ? ? ? ? 0 0 0 ? ? ? 0 0 0 ? ? ? 0 0
0 0 0 0 0 0 ? ? ? 0 0 0 ? ? ? 0 ? ? ? 0 0 0 ? ? ? ? ? ? 0 0
0 0 0 0 ? ? ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? ? ? ? ? ? ? ? ? 0 0
0 0 0 0 ? ? ? 0 0 0 0 0 ? ? ? 0 ? ? ? ? ? ? ? ? ? 0 0 0 ? ?
0 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0 0 ? ? ? ? ? ? ? ? 0 ? ? ? ? ?
0 ? ? ? 0 0 0 0 0 0 0 ? ? ? 0 0 ? ? ? ? ? ? ? ? 0 ? ? ? ? ?
0 ? ? ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? ? ? ? 0 0
0 ? ? ? ? ? ? ? ? ? 0 ? ? ? ? 0 0 ? ? ? ? 0 ? ? ? 0 0 0 0 0
? ? 0 ? ? ? ? ? ? ? 0 ? ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? 0 0 0 0
? ? 0 0 0 0 ? ? ? ? 0 ? ? ? ? 0 0 0 ? ? ? 0 0 ? ? ? 0 0 0 0
? ? 0 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0 0 0 0 0 0 0 ? ? ? ? 0 0 0
0 0 0 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 ? ? ? 0 ? ? ? ? 0 0 0
? ? ? ? 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 ? ? ? 0 ? ? ?
? ? ? ? ? ? ? 0 ? ? ? 0 0 ? ? ? ? ? 0 ? ? ? ? ? ? ? 0 ? ? ?
? ? ? ? ? ? ? 0 ? ? ? ? 0 ? ? ? ? ? 0 0 0 0 ? ? ? 0 0 ? ? ?
0 0 ? ? ? ? ? 0 ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? 0 0 0 0 0
0 0 ? ? ? ? ? 0 0 ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 0 0
0 0 0 0 ? ? ? 0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 ? ? ? ? ? ? ? 0 0 ? ? ? ? ? ? ? ? 0 0 0 0
0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ?
0 0 0 0 0 ? ? ? ? ? ? ? 0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ?
0 0 0 0 0 ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ?
""",#87
"""
? ? ? 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? ? 0
? ? ? 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? ? 0
? ? ? 0 ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? ? 0
? ? ? 0 ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 ? ? ? ? 0 0 0 0
? ? ? ? ? ? ? 0 0 ? ? ? ? ? ? ? ? ? ? 0 0 0 ? ? ? ? 0 0 0 0
0 0 ? ? ? ? ? 0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ? ? 0 0 0 0 0
0 0 ? ? ? ? 0 ? ? ? ? ? 0 0 ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0
0 ? ? ? ? ? ? ? ? ? 0 0 0 0 0 ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0
? ? ? ? 0 0 ? ? ? ? 0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? ? 0 0
? ? ? ? 0 0 ? ? ? ? ? ? ? 0 0 ? ? ? ? ? 0 ? ? ? ? ? ? ? 0 0
? ? 0 0 0 0 0 ? ? ? ? ? ? 0 0 ? ? ? ? ? 0 0 0 ? ? ? ? ? 0 0
0 0 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 0 ? ? ? 0 0 0 ? ? ? ? 0 0 0
0 0 0 0 0 0 0 ? ? ? ? ? ? 0 0 0 0 ? ? ? 0 0 0 ? ? ? 0 0 0 0
0 0 0 0 0 0 0 ? ? ? ? ? 0 0 0 0 0 0 0 0 0 0 0 ? ? ? 0 0 0 0
? ? 0 0 0 0 0 ? ? ? ? ? ? 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ?
? ? 0 0 0 0 0 0 0 0 ? ? ? 0 0 ? ? ? 0 0 ? ? ? ? ? ? 0 ? ? ?
? ? 0 0 ? ? ? 0 0 0 ? ? ? 0 0 ? ? ? 0 0 ? ? ? ? ? ? 0 ? ? ?
0 0 0 0 ? ? ? 0 ? ? ? 0 0 0 0 ? ? ? 0 0 ? ? ? ? ? ? 0 0 ? ?
0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? ? ? ? 0 0 0 0
0 0 0 0 0 0 ? ? ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? ? ? ? ? ? ? 0
0 0 0 0 0 0 ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 ? ? ? ? ? ? ? ? 0
0 ? ? ? ? ? 0 0 ? ? ? 0 0 0 0 0 0 ? ? ? ? ? ? ? ? ? ? ? ? 0
0 ? ? ? ? ? 0 0 ? ? ? 0 0 0 0 0 0 ? ? ? ? ? ? ? 0 ? ? ? ? 0
0 ? ? ? ? ? 0 0 0 0 0 0 0 0 0 0 0 ? ? ? ? ? 0 ? ? ? ? ? ? 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ? ? ? 0 0
0 ? ? ? 0 0 0 0 ? ? ? 0 0 0 ? ? ? 0 0 0 0 0 0 ? ? ? 0 ? ? ?
? ? ? ? 0 0 0 0 ? ? ? 0 0 0 ? ? ? 0 0 0 0 ? ? ? ? ? 0 ? ? ?
? ? ? ? 0 0 0 0 ? ? ? 0 0 0 ? ? ? ? ? 0 0 ? ? ? ? ? ? ? ? ?
? ? 0 ? ? ? 0 0 ? ? ? 0 0 0 0 0 ? ? ? 0 0 ? ? ? ? ? ? ? ? ?
0 0 0 ? ? ? 0 0 ? ? ? 0 0 0 0 0 ? ? ? 0 0 0 0 0 0 0 ? ? ? ?
""",#90
"""
? ? ? 0 0 ? ? ? ? ? ? 0 0 ? ? ? ?
? ? ? 0 0 ? ? ? ? ? ? 0 0 ? ? ? ?
0 0 0 0 0 ? ? ? ? 0 0 0 0 0 ? ? ?
0 0 0 0 0 0 ? ? ? 0 0 0 0 0 ? ? ?
0 0 0 0 0 0 0 0 0 0 0 0 0 0 ? ? ?
? ? ? 0 0 0 0 0 0 0 0 0 0 ? ? ? ?
? ? ? 0 0 0 0 0 0 0 0 0 0 ? ? ? ?
""",
"""
? ? ?
? ? ?
? ? ?
""",
"""
?
"""
]
nums = [6, 43, 0, 45, 87, 90, 12, 8, 1]

def open(i, j):
	return [x.split(' ') for x in result[which].split('\n') if x != ''][i][j]

from itertools import combinations
from copy import deepcopy

def surrounding(matrix, i, j, r, c):
	i_s = [i] + ([i - 1] if i != 0 else []) + ([i + 1] if i != r - 1 else [])
	j_s = [j] + ([j - 1] if j != 0 else []) + ([j + 1] if j != c - 1 else [])
	return list(filter(lambda x: matrix[x[0]][x[1]] == '?', [(x, y) for x in i_s for y in j_s]))

def surrounding_mine(matrix, i, j, r, c):
	i_s = [i] + ([i - 1] if i != 0 else []) + ([i + 1] if i != r - 1 else [])
	j_s = [j] + ([j - 1] if j != 0 else []) + ([j + 1] if j != c - 1 else [])
	return len(list(filter(lambda x: matrix[x[0]][x[1]] == 'x', [(x, y) for x in i_s for y in j_s])))

def sub_click0(matrix, i, j, r, c, not_0list):
	for x, y in surrounding(matrix, i, j, r, c):
		matrix[x][y] = str(open(x, y))
		if matrix[x][y] != '0':
			not_0list.append((x,y))
	return not_0list

def click0(matrix, r, c):
	not_0list = []
	for i in range(r):
		for j in range(c):
			if matrix[i][j] != '0':
				continue
			not_0list = sub_click0(matrix, i, j, r, c, not_0list)
	return not_0list

def simpleFindMine(matrix, totalposlist, r, c):
	temp = []
	change = True
	while change:
		change = False
		for pos in totalposlist:
			surr = surrounding(matrix, pos[0], pos[1], r, c)
			if len(surr) == eval(matrix[pos[0]][pos[1]]) - surrounding_mine(matrix, pos[0], pos[1], r, c):
				for surrpos in surr:
					matrix[surrpos[0]][surrpos[1]] = 'x'
					change = True
	for pos in totalposlist:
		surr = surrounding(matrix, pos[0], pos[1], r, c)
		if eval(matrix[pos[0]][pos[1]]) == surrounding_mine(matrix, pos[0], pos[1], r, c):
			for surrpos in surr:
				matrix[surrpos[0]][surrpos[1]] = str(open(surrpos[0], surrpos[1]))
				temp.append((surrpos[0], surrpos[1]))
				change = True
	return matrix, change, temp

def BruteSearch(matrix, r, c, numofmine):
	opened = list(filter(lambda x: len(surrounding(matrix, x[0], x[1], r, c)) != 0 and matrix[x[0]][x[1]] not in ('x', '?'), [(i, j) for i in range(r) for j in range(c)]))
	openedsurr = {(i ,j):set(surrounding(matrix, i, j, r, c)) for i, j in opened}
	surr = set()
	for op in opened:
		surr = surr | openedsurr[op]
	numofsurr = len(surr)
	needmine = {(i, j):eval(matrix[i][j]) - surrounding_mine(matrix, i, j, r, c) for i, j in opened}
	unopened = 0
	for i in range(r):
		for j in range(c):
			unopened += 1 if matrix[i][j] == '?' else 0
	ret = []
	possible = Recursion(opened, openedsurr, needmine, numofmine)
	for exist in possible:
		if unopened - numofsurr < numofmine - len(exist):
			continue
		ret.append(exist)
	never = surr
	change = False
	ret2 = ret
	ret = []
	for exist in ret2:
		fail = False
		for op in opened:
			if len(openedsurr[op] & set(exist)) != needmine[op]:
				fail = True
				change = True
				break
		if not fail:
			ret.append(exist)
	for exist in ret:
		never = never - set(exist)
	for i, j in never:
		matrix[i][j] = str(open(i ,j))
		change = True
	always = None
	for exist in ret:
		if always == None:
			always = set(exist)
		always = always & set(exist)
	if always != None:
		for i, j in always:
			matrix[i][j] = 'x'
			numofmine -= 1
			change = True
	return ret, change, numofmine

def Recursion(opened, openedsurr, needmine, numofmine):
	possible = {():()}
	for op in opened:
		temp = {}
		for exist in possible:
			prohibit = set(possible[exist])
			exist = set(exist)
			already = len(exist & openedsurr[op])
			if already > needmine[op]:
				continue
			for choice in combinations(openedsurr[op], needmine[op] - already):
				choice = set(choice)
				if len(choice & prohibit) > 0:
					continue
				temp[tuple(exist | choice)] = tuple(prohibit | (openedsurr[op] - choice))
		possible = temp
	return list(filter(lambda x: len(x) <= numofmine, possible.keys()))

def check(matrix, r, c):
	ret = True
	for i in range(r):
		for j in range(c):
			if matrix[i][j] in 'x?':
				continue
			if matrix[i][j] != str(surrounding_mine(matrix, i, j, r, c)):
				ret = False
				break
		if not ret:
			break
	return ret

def countMine(matrix, r, c, chars):
	numofmine = 0
	for i in range(r):
		for j in range(c):
			numofmine += 1 if matrix[i][j] == chars else 0
	return numofmine

def solve_mine(map, n):
	matrix = [x.split(' ') for x in map.split('\n') if x != '']
	r, c = len(matrix), len(matrix[0])
	totalposlist = []
	change = True
	while change:
		poslist = click0(matrix, r, c)
		totalposlist.extend(poslist)
		matrix, change, poslist = simpleFindMine(matrix, totalposlist, r, c)
		totalposlist.extend(poslist)
	numofmine = n - countMine(matrix, r, c, 'x')
	change = True
	while change:
		change = False
		possible, change, numofmine = BruteSearch(matrix, r, c, numofmine)
	has_ret = False
	for mines in possible:
		temp = deepcopy(matrix)
		for i, j in mines:
			temp[i][j] = 'x'
		for i, j in mines:
			temp[i][j] = 'x'
		if countMine(temp, r, c, 'x') + countMine(temp, r, c, '?') == n:
			for i in range(r):
				for j in range(c):
					if temp[i][j] == '?':
						temp[i][j] = 'x'
			return '\n'.join(' '.join(x) for x in temp)
		elif countMine(temp, r, c, 'x') + countMine(temp, r, c, '?') > n:
			return '?'
		else:
			for i in range(r):
				for j in range(c):
					if temp[i][j] == '?':
						temp[i][j] = str(surrounding_mine(temp, i, j, r, c))
		'''if check(temp, r, c):
			print('Possible\n' + '\n'.join(' '.join(x[-4:]) for x in temp), '\n')
		'''
		if check(temp, r, c) and not has_ret:
			ret = temp
			has_ret = True
		elif check(temp, r, c) and has_ret:
			return '?'
	return '\n'.join(' '.join(x) for x in ret)

global which
which = 8
sov = solve_mine(maps[which], nums[which])
print(sov)
'''for i, j in mines:
			temp[i][j] = 'x'
		if countMine(temp, r, c, 'x') + countMine(temp, r, c, '?') == n:
			for i in range(r):
				for j in range(c):
					if temp[i][j] == '?':
						temp[i][j] = 'x'
			return '\n'.join(' '.join(x) for x in temp)
		elif countMine(temp, r, c, 'x') + countMine(temp, r, c, '?') > n:
			return '?'
		else:'''
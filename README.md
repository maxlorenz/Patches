# Patches
Small script to mix patches to maximize their distance

Takes an 2x2 matrix of image patches and maximizes their distance to their respective origin as well as to their original neighbors. It uses a simple swap-random-if-better algorithm.

## Example output for 47x5, for 3cmx4.5cm patches with 500.000 swaps

Stats:
```
Initial distance: 472.4
Total distance: 21970.2292187
```

Patches:
```
Number: 1 Row: 21 Column: 3
Number: 2 Row: 34 Column: 5
Number: 3 Row: 21 Column: 1
Number: 4 Row: 24 Column: 4
Number: 5 Row: 34 Column: 2
Number: 6 Row: 20 Column: 4
Number: 7 Row: 33 Column: 2
Number: 8 Row: 20 Column: 5
Number: 9 Row: 26 Column: 1
Number: 10 Row: 31 Column: 3
Number: 11 Row: 19 Column: 4
Number: 12 Row: 37 Column: 2
Number: 13 Row: 18 Column: 4
Number: 14 Row: 35 Column: 2
Number: 15 Row: 18 Column: 5
Number: 16 Row: 36 Column: 2
Number: 17 Row: 17 Column: 4
Number: 18 Row: 26 Column: 5
Number: 19 Row: 32 Column: 1
Number: 20 Row: 17 Column: 5
Number: 21 Row: 33 Column: 3
Number: 22 Row: 17 Column: 3
Number: 23 Row: 37 Column: 4
Number: 24 Row: 16 Column: 3
Number: 25 Row: 32 Column: 4
Number: 26 Row: 23 Column: 3
Number: 27 Row: 14 Column: 4
Number: 28 Row: 31 Column: 4
Number: 29 Row: 13 Column: 2
Number: 30 Row: 31 Column: 5
Number: 31 Row: 25 Column: 3
Number: 32 Row: 15 Column: 3
Number: 33 Row: 30 Column: 5
Number: 34 Row: 14 Column: 2
Number: 35 Row: 30 Column: 4
Number: 36 Row: 13 Column: 1
Number: 37 Row: 29 Column: 5
Number: 38 Row: 16 Column: 1
Number: 39 Row: 22 Column: 5
Number: 40 Row: 28 Column: 2
Number: 41 Row: 12 Column: 3
Number: 42 Row: 28 Column: 3
Number: 43 Row: 22 Column: 4
Number: 44 Row: 15 Column: 1
Number: 45 Row: 28 Column: 4
Number: 46 Row: 12 Column: 2
Number: 47 Row: 27 Column: 3
Number: 48 Row: 35 Column: 4
Number: 49 Row: 14 Column: 1
Number: 50 Row: 28 Column: 5
Number: 51 Row: 40 Column: 1
Number: 52 Row: 10 Column: 4
Number: 53 Row: 46 Column: 1
Number: 54 Row: 11 Column: 5
Number: 55 Row: 42 Column: 1
Number: 56 Row: 23 Column: 4
Number: 57 Row: 10 Column: 5
Number: 58 Row: 41 Column: 2
Number: 59 Row: 9 Column: 5
Number: 60 Row: 44 Column: 2
Number: 61 Row: 8 Column: 4
Number: 62 Row: 43 Column: 2
Number: 63 Row: 9 Column: 3
Number: 64 Row: 43 Column: 4
Number: 65 Row: 23 Column: 2
Number: 66 Row: 7 Column: 5
Number: 67 Row: 45 Column: 1
Number: 68 Row: 1 Column: 4
Number: 69 Row: 44 Column: 3
Number: 70 Row: 1 Column: 2
Number: 71 Row: 45 Column: 4
Number: 72 Row: 2 Column: 1
Number: 73 Row: 27 Column: 5
Number: 74 Row: 41 Column: 1
Number: 75 Row: 7 Column: 3
Number: 76 Row: 42 Column: 4
Number: 77 Row: 20 Column: 2
Number: 78 Row: 5 Column: 5
Number: 79 Row: 39 Column: 3
Number: 80 Row: 8 Column: 2
Number: 81 Row: 44 Column: 5
Number: 82 Row: 7 Column: 2
Number: 83 Row: 39 Column: 5
Number: 84 Row: 3 Column: 1
Number: 85 Row: 38 Column: 5
Number: 86 Row: 25 Column: 2
Number: 87 Row: 5 Column: 4
Number: 88 Row: 38 Column: 4
Number: 89 Row: 7 Column: 4
Number: 90 Row: 33 Column: 1
Number: 91 Row: 26 Column: 4
Number: 92 Row: 5 Column: 1
Number: 93 Row: 37 Column: 5
Number: 94 Row: 11 Column: 2
Number: 95 Row: 21 Column: 2
Number: 96 Row: 42 Column: 5
Number: 97 Row: 24 Column: 2
Number: 98 Row: 13 Column: 5
Number: 99 Row: 42 Column: 2
Number: 100 Row: 11 Column: 4
Number: 101 Row: 47 Column: 1
Number: 102 Row: 12 Column: 5
Number: 103 Row: 28 Column: 1
Number: 104 Row: 40 Column: 4
Number: 105 Row: 10 Column: 2
Number: 106 Row: 40 Column: 3
Number: 107 Row: 2 Column: 3
Number: 108 Row: 42 Column: 3
Number: 109 Row: 3 Column: 2
Number: 110 Row: 46 Column: 4
Number: 111 Row: 1 Column: 1
Number: 112 Row: 40 Column: 5
Number: 113 Row: 29 Column: 1
Number: 114 Row: 1 Column: 5
Number: 115 Row: 47 Column: 2
Number: 116 Row: 1 Column: 3
Number: 117 Row: 47 Column: 4
Number: 118 Row: 4 Column: 2
Number: 119 Row: 45 Column: 5
Number: 120 Row: 19 Column: 1
Number: 121 Row: 8 Column: 5
Number: 122 Row: 45 Column: 2
Number: 123 Row: 4 Column: 3
Number: 124 Row: 41 Column: 4
Number: 125 Row: 27 Column: 2
Number: 126 Row: 3 Column: 3
Number: 127 Row: 46 Column: 3
Number: 128 Row: 6 Column: 3
Number: 129 Row: 45 Column: 3
Number: 130 Row: 5 Column: 2
Number: 131 Row: 39 Column: 4
Number: 132 Row: 19 Column: 3
Number: 133 Row: 4 Column: 5
Number: 134 Row: 38 Column: 2
Number: 135 Row: 4 Column: 4
Number: 136 Row: 36 Column: 1
Number: 137 Row: 19 Column: 5
Number: 138 Row: 8 Column: 1
Number: 139 Row: 36 Column: 5
Number: 140 Row: 4 Column: 1
Number: 141 Row: 29 Column: 4
Number: 142 Row: 33 Column: 5
Number: 143 Row: 24 Column: 1
Number: 144 Row: 16 Column: 5
Number: 145 Row: 44 Column: 1
Number: 146 Row: 11 Column: 3
Number: 147 Row: 47 Column: 3
Number: 148 Row: 10 Column: 3
Number: 149 Row: 43 Column: 1
Number: 150 Row: 23 Column: 5
Number: 151 Row: 10 Column: 1
Number: 152 Row: 46 Column: 5
Number: 153 Row: 9 Column: 1
Number: 154 Row: 44 Column: 4
Number: 155 Row: 9 Column: 2
Number: 156 Row: 47 Column: 5
Number: 157 Row: 6 Column: 1
Number: 158 Row: 43 Column: 5
Number: 159 Row: 22 Column: 1
Number: 160 Row: 6 Column: 5
Number: 161 Row: 46 Column: 2
Number: 162 Row: 5 Column: 3
Number: 163 Row: 43 Column: 3
Number: 164 Row: 2 Column: 2
Number: 165 Row: 41 Column: 3
Number: 166 Row: 6 Column: 2
Number: 167 Row: 41 Column: 5
Number: 168 Row: 27 Column: 1
Number: 169 Row: 2 Column: 5
Number: 170 Row: 40 Column: 2
Number: 171 Row: 9 Column: 4
Number: 172 Row: 20 Column: 1
Number: 173 Row: 38 Column: 3
Number: 174 Row: 3 Column: 4
Number: 175 Row: 39 Column: 2
Number: 176 Row: 2 Column: 4
Number: 177 Row: 39 Column: 1
Number: 178 Row: 8 Column: 3
Number: 179 Row: 38 Column: 1
Number: 180 Row: 26 Column: 2
Number: 181 Row: 6 Column: 4
Number: 182 Row: 37 Column: 1
Number: 183 Row: 3 Column: 5
Number: 184 Row: 34 Column: 1
Number: 185 Row: 25 Column: 5
Number: 186 Row: 7 Column: 1
Number: 187 Row: 35 Column: 5
Number: 188 Row: 11 Column: 1
Number: 189 Row: 24 Column: 3
Number: 190 Row: 21 Column: 5
Number: 191 Row: 35 Column: 1
Number: 192 Row: 20 Column: 3
Number: 193 Row: 37 Column: 3
Number: 194 Row: 18 Column: 3
Number: 195 Row: 36 Column: 3
Number: 196 Row: 21 Column: 4
Number: 197 Row: 25 Column: 1
Number: 198 Row: 32 Column: 5
Number: 199 Row: 19 Column: 2
Number: 200 Row: 36 Column: 4
Number: 201 Row: 18 Column: 2
Number: 202 Row: 34 Column: 4
Number: 203 Row: 18 Column: 1
Number: 204 Row: 33 Column: 4
Number: 205 Row: 17 Column: 1
Number: 206 Row: 25 Column: 4
Number: 207 Row: 32 Column: 2
Number: 208 Row: 17 Column: 2
Number: 209 Row: 35 Column: 3
Number: 210 Row: 15 Column: 2
Number: 211 Row: 34 Column: 3
Number: 212 Row: 14 Column: 3
Number: 213 Row: 32 Column: 3
Number: 214 Row: 22 Column: 2
Number: 215 Row: 14 Column: 5
Number: 216 Row: 31 Column: 2
Number: 217 Row: 15 Column: 4
Number: 218 Row: 31 Column: 1
Number: 219 Row: 24 Column: 5
Number: 220 Row: 16 Column: 2
Number: 221 Row: 30 Column: 1
Number: 222 Row: 16 Column: 4
Number: 223 Row: 30 Column: 2
Number: 224 Row: 12 Column: 4
Number: 225 Row: 30 Column: 3
Number: 226 Row: 13 Column: 3
Number: 227 Row: 22 Column: 3
Number: 228 Row: 29 Column: 3
Number: 229 Row: 13 Column: 4
Number: 230 Row: 29 Column: 2
Number: 231 Row: 15 Column: 5
Number: 232 Row: 23 Column: 1
Number: 233 Row: 27 Column: 4
Number: 234 Row: 12 Column: 1
Number: 235 Row: 26 Column: 3
```

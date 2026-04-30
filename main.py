import random


class MatrixProcessor:
    def execute(self):
        try:
            r1, c1, r2, c2 = 3, 3, 3, 3

            a = []
            for i in range(r1):
                row = []
                for j in range(c1):
                    row.append(float(random.randint(0, 100)))
                a.append(row)

            b = []
            for i in range(r2):
                row = []
                for j in range(c2):
                    row.append(float(random.randint(0, 100)))
                b.append(row)

            if len(a) != len(b) or len(a[0]) != len(b[0]):
                raise ValueError("Різні розміри")

            res_c = []
            for i in range(len(a)):
                new_row = []
                for j in range(len(a[0])):
                    v1 = int(a[i][j])
                    v2 = int(b[i][j])
                    new_row.append(float(v1 ^ v2))
                res_c.append(new_row)

            print("Матриця A:")
            for r in a: print(r)
            print("\nМатриця B:")
            for r in b: print(r)
            print("\nМатриця C (A XOR B):")
            for r in res_c: print(r)

            total_sum = 0.0
            for j in range(len(res_c[0])):
                min_val = res_c[0][j]
                for i in range(1, len(res_c)):
                    if res_c[i][j] < min_val:
                        min_val = res_c[i][j]
                total_sum += min_val

            print("\nРезультат:", total_sum)

        except Exception as e:
            print(f"Помилка: {e}")


if __name__ == "__main__":
    processor = MatrixProcessor()
    processor.execute()

class Matrix:
    def __init__(self, matrix_string):
        self.rows = []
        self.columns = []
        rows = matrix_string.split('\n')
        for row in rows:
            values = row.split(' ')
            if not self.columns:
                for j in range(0, len(values)):
                    self.columns.append([])
            build_row = []
            i = 0
            for value in values:
                build_row.append(int(value))
                self.columns[i].append(int(value))
                i += 1
            self.rows.append(build_row)

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]

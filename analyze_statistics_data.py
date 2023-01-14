class analyze_statistics_data:
    def analyze(students):
        print(students.describe())
        print(students.info())
        print(students.isnull().values.any())



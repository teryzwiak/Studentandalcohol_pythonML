import matplotlib.pyplot as plt
import seaborn as sns
class correlations:
    def show(students):
        correlations = students.corr()
        fig, ax = plt.subplots(figsize=(15, 15))

        colormap = sns.color_palette("BrBG", 10)

        sns.heatmap(correlations, 
            cmap=colormap, 
            annot=True, 
            fmt=".2f")

        plt.show()
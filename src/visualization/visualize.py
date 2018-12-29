# plot frequency of each label
def plot_label_frequency(X, label_column):
    # create dataframe with labels
    label_df = X.groupby(label_column).size().reset_index()
    label_df.columns = ['label', 'frequency']
    # plot barchart of label frequency
    plt.bar(label_df['label'], label_df['frequency'], align='center', alpha=0.5)
    plt.title('Frequency of ')
    plt.show()
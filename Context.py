import pandas as pd


def set_pandas_options(DataFrame):
    """
    Set up pandas options to show the shape of the dataframe

    Parameters
    ----------
    DataFrame : Original data

    """
    pd.set_option('display.max_rows', DataFrame.shape[0] + 1)
    pd.set_option('display.expand_frame_repr', False)


def select_cols(DataFrame):
    """
    Replace the original dataframe with the selected columns

    Parameters
    ----------
    DataFrame : Original data

    Returns
    -------
    DataFrame : Updated data

    """

    # Print original column names
    print("Initial columns")
    print(DataFrame.columns)

    # Select the columns that will be used
    selected_cols = DataFrame[['name',
                               'recclass',
                               'mass (g)',
                               'fall',
                               'year',
                               'reclat',
                               'reclong',
                               'GeoLocation']]
    DataFrame = selected_cols.copy()
    print("Selected columns")
    print(DataFrame.columns)
    return DataFrame


def check_missing_values(DataFrame):
    """
    Replace the original dataframe with the selected columns

    Parameters
    ----------
    DataFrame : Original data

    Returns
    -------
    DataFrame : Updated data

    """

    # Check the missing value in the original dataframe
    print(DataFrame.isna().any())

    # Drop the rows with missing value
    DataFrame = DataFrame.dropna(axis=0, how='any')

    # Check the missing value again
    print(DataFrame.isna().any())
    return DataFrame


def sort_data(DataFrame):
    """
    Rearrange the data according to the name

    Parameters
    ----------
    DataFrame : Original data

    Returns
    -------
    DataFrame : Updated data

    """

    DataFrame = DataFrame.sort_values(by='name', ascending=True)
    DataFrame.index = DataFrame['name']
    DataFrame = DataFrame.drop(['name'], axis=1)
    return DataFrame


def time_reformat(DataFrame):
    """
    Change the format in "year" column, maintain the year information

    Parameters
    ----------
    DataFrame : Original data

    Returns
    -------
    DataFrame : Updated data

    """

    # (dataframe, 2021)
    DataFrame['year'] = DataFrame['year'].astype(str).str[6:10]
    return DataFrame


if __name__ == '__main__':
    # Load the data set from local document
    df = pd.read_csv('Meteorite_Landings.csv')

    set_pandas_options(df)
    df = select_cols(df)
    df = check_missing_values(df)
    df = sort_data(df)
    df = time_reformat(df)

    # Display the information of the prepared data
    print(df)
    print('The shape of the dataframe: {}'.format(df.shape))
    print('The size of the dataframe : {}'.format(df.size))
    print(df.info(verbose=True))

    # Save the prepared as a new csv file
    df.to_csv('Prepared data set.csv')

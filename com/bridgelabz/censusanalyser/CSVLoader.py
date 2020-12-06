from com.bridgelabz.censusanalyser.CensusAnalyser import CensusAnalyzer
from com.bridgelabz.censusanalyser.CensusAnalyserStateCode import CensusAnalyserStateCode
from com.bridgelabz.censusanalyser.CensusAnalysisException import CensusAnalysisException
from com.bridgelabz.censusanalyser.CensusAnalysisHeader import CensusAnalysisHeader


class CSVLoader(CensusAnalyzer):

    def record_counter(self):
        try:
            return super(CSVLoader, self).record_counter()
        except FileNotFoundError:
            raise CensusAnalysisException("Invalid File Path")
        except ValueError:
            raise CensusAnalysisException("Wrong Delimiter or Invalid Columns Name")


if __name__ == "__main__":
    path_csv_file = "C:/Users/SRS/Downloads/IndiaStateCensusAnalyser/Data/IndiaStateCensusData.csv"
    path_statecode_file = "C:/Users/SRS/Downloads/IndiaStateCensusAnalyser/Data1/IndiaStateCode.csv"
    read_csvfile = CSVLoader(path_csv_file,obj=CensusAnalysisHeader())
    read_statecode = CSVLoader(path_statecode_file, obj=CensusAnalyserStateCode())
    print(read_csvfile.record_counter())
    print(read_statecode.record_counter())
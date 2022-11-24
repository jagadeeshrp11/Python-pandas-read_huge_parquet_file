# Genaral Process, Reading parquet file using read_parquet with pyarrow.
df = pd.read_parquet(File_name,engine="pyarrow")
df.columns
Traceback (most recent call last):
  File "C:\Users\egderja\AppData\Local\Programs\Python\Python39\lib\code.py", line 90, in runcode
    exec(code, self.locals)
  File "<input>", line 1, in <module>
  File "C:\Users\egderja\OneDrive - Ericsson\Laptop\pych\venv\lib\site-packages\pandas\io\parquet.py", line 503, in read_parquet
    return impl.read(
  File "C:\Users\egderja\OneDrive - Ericsson\Laptop\pych\venv\lib\site-packages\pandas\io\parquet.py", line 251, in read
    result = self.api.parquet.read_table(
  File "pyarrow\array.pxi", line 830, in pyarrow.lib._PandasConvertible.to_pandas
  File "pyarrow\table.pxi", line 3908, in pyarrow.lib.Table._to_pandas
  File "C:\Users\egderja\OneDrive - Ericsson\Laptop\pych\venv\lib\site-packages\pyarrow\pandas_compat.py", line 820, in table_to_blockmanager
    blocks = _table_to_blocks(options, table, categories, ext_columns_dtypes)
  File "C:\Users\egderja\OneDrive - Ericsson\Laptop\pych\venv\lib\site-packages\pyarrow\pandas_compat.py", line 1170, in _table_to_blocks
    result = pa.lib.table_to_blocks(options, block_table, categories,
  File "pyarrow\table.pxi", line 2594, in pyarrow.lib.table_to_blocks
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 2.59 GiB for an array with shape (58, 5995368) and data type object

# Read parquet file using pyarrow.parquet
import pyarrow.parquet as pq
parquet_file = pq.ParquetFile(File_path)
for batch in parquet_file.iter_batches():
    batch_df = batch.to_pandas()
    print(" Length : "+str(len(batch_df)))

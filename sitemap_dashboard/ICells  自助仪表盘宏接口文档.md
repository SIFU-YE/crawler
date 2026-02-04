com.aspose.cells.Cells
### Hierarchy 层级
## Index 目录
###  Methods 方法 
  * applyColumnStyle
  * applyRowStyle
  * applyStyle
  * checkColumn
  * clearContents
  * clearFormats
  * clearRange
  * convertStringToNumericValue
  * copyColumn
  * copyColumns
  * createRange
  * deleteBlankColumns
  * deleteBlankRows
  * deleteColumn
  * deleteColumns
  * deleteRange
  * deleteRows
  * endCellInColumn
  * endCellInRow
  * exportArray
  * exportTypeArray
  * findFormula
  * findFormulaContains
  * getCellStyle
  * getColumnWidth
  * getColumnWidthInch
  * getColumnWidthPixel
  * getColumns
  * getCountLarge
  * getDependents
  * getFirstCell
  * getGroupedColumnOutlineLevel
  * getGroupedRowOutlineLevel
  * getLastCell
  * getLastDataRow
  * getMaxColumn
  * getMaxDataColumn
  * getMaxDataRow
  * getMaxDisplayRange
  * getMaxGroupedColumnOutlineLevel
  * getMaxGroupedRowOutlineLevel
  * getMemorySetting
  * getMergedCells
  * getMinColumn
  * getMinDataColumn
  * getMinDataRow
  * getMultiThreadReading
  * getOdsCellFields
  * getPreserveString
  * getRowEnumerator
  * getRowHeight
  * getRowHeightInch
  * getRowHeightPixel
  * getStandardHeight
  * getStandardHeightPixels
  * getStandardWidth
  * getStandardWidthInch
  * getStandardWidthPixels
  * getViewColumnWidthPixel
  * getViewRowHeight
  * getViewRowHeightInch
  * groupColumns
  * hideColumn
  * hideColumns
  * hideGroupDetail
  * importArray
  * importArrayList
  * importCustomObjects
  * importData
  * importFormulaArray
  * importObjectArray
  * importResultSet
  * importTwoDimensionArray
  * insertColumn
  * insertColumns
  * insertCutCells
  * insertRange
  * insertRows
  * isBlankColumn
  * isColumnHidden
  * isDefaultRowHeightMatched
  * isDefaultRowHidden
  * isDeletingRangeEnabled
  * isRowHidden
  * linkToXmlMap
  * removeDuplicates
  * removeFormulas
  * retrieveSubtotalSetting
  * setColumnWidth
  * setColumnWidthInch
  * setColumnWidthPixel
  * setDefaultRowHeightMatched
  * setDefaultRowHidden
  * setMemorySetting
  * setMultiThreadReading
  * setPreserveString
  * setRowHeight
  * setRowHeightInch
  * setRowHeightPixel
  * setStandardHeight
  * setStandardHeightPixels
  * setStandardWidth
  * setStandardWidthInch
  * setStandardWidthPixels
  * setViewColumnWidthPixel
  * showGroupDetail
  * textToColumns
  * ungroupColumns
  * ungroupRows
  * unhideColumn
  * unhideColumns
  * unhideRows


##  Methods 方法 
###  addRange 
  * addRange(rangeObjectIRange)void


  * void addRange(com.aspose.cells.Range)
#### Parameters 参数
    * #####  rangeObject: IRange
####  Returns 返回值 void


###  applyColumnStyle 
  * applyColumnStyle(columnnumber, styleIStyle, flagIStyleFlag)void


  * void applyColumnStyle(int, com.aspose.cells.Style, com.aspose.cells.StyleFlag)
#### Parameters 参数
    * #####  column: number
    * #####  style: IStyle
    * ####  Returns 返回值 void


###  applyRowStyle 
  * applyRowStyle(rownumber, styleIStyle, flagIStyleFlag)void


  * void applyRowStyle(int, com.aspose.cells.Style, com.aspose.cells.StyleFlag)
#### Parameters 参数
    * #####  row: number
    * #####  style: IStyle
    * ####  Returns 返回值 void


###  applyStyle 
  * applyStyle(styleIStyle, flagIStyleFlag)void


  * void applyStyle(com.aspose.cells.Style, com.aspose.cells.StyleFlag)
#### Parameters 参数
    * #####  style: IStyle
    * ####  Returns 返回值 void


###  checkCell 
  * checkCell(rownumber, columnnumber)ICell


  * com.aspose.cells.Cell checkCell(int, int)
#### Parameters 参数
    * #####  row: number
    * #####  column: number
####  Returns 返回值 ICell


###  checkColumn 
  * checkColumn(columnIndexnumber)IColumn


  * com.aspose.cells.Column checkColumn(int)
#### Parameters 参数
    * #####  columnIndex: number
####  Returns 返回值 IColumn


###  check 
  * checkRow(rownumber)IRow


  * com.aspose.cells.Row checkRow(int)
#### Parameters 参数
    * #####  row: number
####  Returns 返回值 IRow


###  clear 
  * clear()void


  * void clear()
####  Returns 返回值 void


###  clearContents 
  * clearContents(startRownumber, startColumnnumber, endRownumber, endColumnnumber)void
  * clearContents(rangeICellArea)void


  * void clearContents(int, int, int, int)
#### Parameters 参数
    * #####  startRow: number
    * #####  startColumn: number
    * #####  endRow: number
    * #####  endColumn: number
####  Returns 返回值 void
  * void clearContents(com.aspose.cells.CellArea)
#### Parameters 参数
    * #####  range: ICellArea
####  Returns 返回值 void


###  clearFormats 
  * clearFormats(startRownumber, startColumnnumber, endRownumber, endColumnnumber)void
  * clearFormats(rangeICellArea)void


  * void clearFormats(int, int, int, int)
#### Parameters 参数
    * #####  startRow: number
    * #####  startColumn: number
    * #####  endRow: number
    * #####  endColumn: number
####  Returns 返回值 void
  * void clearFormats(com.aspose.cells.CellArea)
#### Parameters 参数
    * #####  range: ICellArea
####  Returns 返回值 void


###  clearRange 
  * clearRange(rangeICellArea)void
  * clearRange(startRownumber, startColumnnumber, endRownumber, endColumnnumber)void


  * void clearRange(com.aspose.cells.CellArea)
#### Parameters 参数
    * #####  range: ICellArea
####  Returns 返回值 void
  * void clearRange(int, int, int, int)
#### Parameters 参数
    * #####  startRow: number
    * #####  startColumn: number
    * #####  endRow: number
    * #####  endColumn: number
####  Returns 返回值 void


###  convertStringToNumericValue 
  * convertStringToNumericValue()void


  * void convertStringToNumericValue()
####  Returns 返回值 void


###  copyColumn 
  * copyColumn(sourceCellsICells, sourceColumnIndexnumber, destinationColumnIndexnumber)void


  * void copyColumn(com.aspose.cells.Cells, int, int)
#### Parameters 参数
    * #####  sourceCells: ICells
    * #####  sourceColumnIndex: number
    * #####  destinationColumnIndex: number
####  Returns 返回值 void


###  copyColumns 
  * copyColumns(sourceCells0ICells, sourceColumnIndexnumber, destinationColumnIndexnumber, columnNumbernumber, pasteOptionsIPasteOptions)void
  * copyColumns(sourceCells0ICells, sourceColumnIndexnumber, destinationColumnIndexnumber, columnNumbernumber)void
  * copyColumns(sourceCellsICells, sourceColumnIndexnumber, sourceTotalColumnsnumber, destinationColumnIndexnumber, destinationTotalColumnsnumber)void


  * void copyColumns(com.aspose.cells.Cells, int, int, int, com.aspose.cells.PasteOptions)
#### Parameters 参数
    * #####  sourceCells0: ICells
    * #####  sourceColumnIndex: number
    * #####  destinationColumnIndex: number
    * #####  columnNumber: number
    * #####  pasteOptions: IPasteOptions
####  Returns 返回值 void
  * void copyColumns(com.aspose.cells.Cells, int, int, int)
#### Parameters 参数
    * #####  sourceCells0: ICells
    * #####  sourceColumnIndex: number
    * #####  destinationColumnIndex: number
    * #####  columnNumber: number
####  Returns 返回值 void
  * void copyColumns(com.aspose.cells.Cells, int, int, int, int)
#### Parameters 参数
    * #####  sourceCells: ICells
    * #####  sourceColumnIndex: number
    * #####  sourceTotalColumns: number
    * #####  destinationColumnIndex: number
    * #####  destinationTotalColumns: number
####  Returns 返回值 void


###  copy 
  * copyRow(sourceCellsICells, sourceRowIndexnumber, destinationRowIndexnumber)void


  * void copyRow(com.aspose.cells.Cells, int, int)
#### Parameters 参数
    * #####  sourceCells: ICells
    * #####  sourceRowIndex: number
    * #####  destinationRowIndex: number
####  Returns 返回值 void


###  copyRows 
  * copyRows(sourceCellsICells, sourceRowIndexnumber, destinationRowIndexnumber, rowNumbernumber)void
  * copyRows(sourceCells0ICells, sourceRowIndexnumber, destinationRowIndexnumber, rowNumbernumber, copyOptionsICopyOptions, pasteOptionsIPasteOptions)void
  * copyRows(sourceCells0ICells, sourceRowIndexnumber, destinationRowIndexnumber, rowNumbernumber, copyOptionsICopyOptions)void


  * void copyRows(com.aspose.cells.Cells, int, int, int)
#### Parameters 参数
    * #####  sourceCells: ICells
    * #####  sourceRowIndex: number
    * #####  destinationRowIndex: number
    * #####  rowNumber: number
####  Returns 返回值 void
  * void copyRows(com.aspose.cells.Cells, int, int, int, com.aspose.cells.CopyOptions, com.aspose.cells.PasteOptions)
#### Parameters 参数
    * #####  sourceCells0: ICells
    * #####  sourceRowIndex: number
    * #####  destinationRowIndex: number
    * #####  rowNumber: number
    * #####  copyOptions: ICopyOptions
    * #####  pasteOptions: IPasteOptions
####  Returns 返回值 void
  * void copyRows(com.aspose.cells.Cells, int, int, int, com.aspose.cells.CopyOptions)
#### Parameters 参数
    * #####  sourceCells0: ICells
    * #####  sourceRowIndex: number
    * #####  destinationRowIndex: number
    * #####  rowNumber: number
    * #####  copyOptions: ICopyOptions
####  Returns 返回值 void


###  createRange 
  * createRange(upperLeftCellstring, lowerRightCellstring)IRange
  * createRange(firstIndexnumber, numbernumber, isVerticalboolean)IRange
  * createRange(firstRownumber, firstColumnnumber, totalRowsnumber, totalColumnsnumber)IRange
  * createRange(addressstring)IRange


  * com.aspose.cells.Range createRange(java.lang.String, java.lang.String)
#### Parameters 参数
    * #####  upperLeftCell: string
    * #####  lowerRightCell: string
####  Returns 返回值 IRange
  * com.aspose.cells.Range createRange(int, int, boolean)
#### Parameters 参数
    * #####  firstIndex: number
    * #####  number: number
    * #####  isVertical: boolean
####  Returns 返回值 IRange
  * com.aspose.cells.Range createRange(int, int, int, int)
#### Parameters 参数
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  totalRows: number
    * #####  totalColumns: number
####  Returns 返回值 IRange
  * com.aspose.cells.Range createRange(java.lang.String)
#### Parameters 参数
    * #####  address: string
####  Returns 返回值 IRange


###  deleteBlankColumns 
  * deleteBlankColumns()void
  * deleteBlankColumns(optionsIDeleteOptions)void


  * void deleteBlankColumns()
####  Returns 返回值 void
  * void deleteBlankColumns(com.aspose.cells.DeleteOptions)
#### Parameters 参数
    * #####  options: IDeleteOptions
####  Returns 返回值 void


###  deleteBlankRows 
  * deleteBlankRows(optionsIDeleteOptions)void
  * deleteBlankRows()void


  * void deleteBlankRows(com.aspose.cells.DeleteOptions)
#### Parameters 参数
    * #####  options: IDeleteOptions
####  Returns 返回值 void
  * void deleteBlankRows()
####  Returns 返回值 void


###  deleteColumn 
  * deleteColumn(columnIndexnumber, updateReferenceboolean)void
  * deleteColumn(columnIndexnumber)void


  * void deleteColumn(int, boolean)
#### Parameters 参数
    * #####  columnIndex: number
    * #####  updateReference: boolean
####  Returns 返回值 void
  * void deleteColumn(int)
#### Parameters 参数
    * #####  columnIndex: number
####  Returns 返回值 void


###  deleteColumns 
  * deleteColumns(columnIndexnumber, totalColumnsnumber, updateReferenceboolean)void


  * void deleteColumns(int, int, boolean)
#### Parameters 参数
    * #####  columnIndex: number
    * #####  totalColumns: number
    * #####  updateReference: boolean
####  Returns 返回值 void


###  deleteRange 
  * deleteRange(startRownumber, startColumnnumber, endRownumber, endColumnnumber, shiftTypenumber)void


  * void deleteRange(int, int, int, int, int)
#### Parameters 参数
    * #####  startRow: number
    * #####  startColumn: number
    * #####  endRow: number
    * #####  endColumn: number
    * #####  shiftType: number
####  Returns 返回值 void


###  delete 
  * deleteRow(rowIndexnumber)void


  * void deleteRow(int)
#### Parameters 参数
    * #####  rowIndex: number
####  Returns 返回值 void


###  deleteRows 
  * deleteRows(rowIndexnumber, totalRowsnumber)boolean
  * deleteRows(rowIndexnumber, totalRowsnumber, updateReferenceboolean)boolean


  * boolean deleteRows(int, int)
#### Parameters 参数
    * #####  rowIndex: number
    * #####  totalRows: number
####  Returns 返回值 boolean
  * boolean deleteRows(int, int, boolean)
#### Parameters 参数
    * #####  rowIndex: number
    * #####  totalRows: number
    * #####  updateReference: boolean
####  Returns 返回值 boolean


###  dispose 
  * dispose()void


  * void dispose()
####  Returns 返回值 void


###  endCellInColumn 
  * endCellInColumn(startRownumber, endRownumber, startColumnnumber, endColumnnumber)ICell
  * endCellInColumn(columnIndexnumber)ICell


  * com.aspose.cells.Cell endCellInColumn(int, int, short, short)
#### Parameters 参数
    * #####  startRow: number
    * #####  endRow: number
    * #####  startColumn: number
    * #####  endColumn: number
####  Returns 返回值 ICell
  * com.aspose.cells.Cell endCellInColumn(short)
#### Parameters 参数
    * #####  columnIndex: number
####  Returns 返回值 ICell


###  endCellInRow 
  * endCellInRow(startRownumber, endRownumber, startColumnnumber, endColumnnumber)ICell
  * endCellInRow(rowIndexnumber)ICell


  * com.aspose.cells.Cell endCellInRow(int, int, int, int)
#### Parameters 参数
    * #####  startRow: number
    * #####  endRow: number
    * #####  startColumn: number
    * #####  endColumn: number
####  Returns 返回值 ICell
  * com.aspose.cells.Cell endCellInRow(int)
#### Parameters 参数
    * #####  rowIndex: number
####  Returns 返回值 ICell


###  exportArray 
  * exportArray(firstRownumber, firstColumnnumber, totalRowsnumber, totalColumnsnumber)any[][]


  * java.lang.Object[][] exportArray(int, int, int, int)
#### Parameters 参数
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  totalRows: number
    * #####  totalColumns: number
####  Returns 返回值 any[][]


###  exportTypeArray 
  * exportTypeArray(firstRownumber, firstColumnnumber, totalRowsnumber, totalColumnsnumber)number[][]


  * int[][] exportTypeArray(int, int, int, int)
#### Parameters 参数
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  totalRows: number
    * #####  totalColumns: number
####  Returns 返回值 number[][]


###  find 
  * find(whatany, previousCellICell)ICell
  * find(whatany, previousCellICell, findOptionsIFindOptions)ICell


  * com.aspose.cells.Cell find(java.lang.Object, com.aspose.cells.Cell)
#### Parameters 参数
    * #####  previousCell: ICell
####  Returns 返回值 ICell
  * com.aspose.cells.Cell find(java.lang.Object, com.aspose.cells.Cell, com.aspose.cells.FindOptions)
#### Parameters 参数
    * #####  previousCell: ICell
    * #####  findOptions: IFindOptions
####  Returns 返回值 ICell


###  findFormula 
  * findFormula(formulastring, previousCellICell)ICell


  * com.aspose.cells.Cell findFormula(java.lang.String, com.aspose.cells.Cell)
#### Parameters 参数
    * #####  formula: string
    * #####  previousCell: ICell
####  Returns 返回值 ICell


###  findFormulaContains 
  * findFormulaContains(formulastring, previousCellICell)ICell


  * com.aspose.cells.Cell findFormulaContains(java.lang.String, com.aspose.cells.Cell)
#### Parameters 参数
    * #####  formula: string
    * #####  previousCell: ICell
####  Returns 返回值 ICell


###  get 
  * get(cellNamestring)ICell
  * get(indexnumber)ICell
  * get(rownumber, columnnumber)ICell


  * com.aspose.cells.Cell get(java.lang.String)
#### Parameters 参数
    * #####  cellName: string
####  Returns 返回值 ICell
  * com.aspose.cells.Cell get(int)
#### Parameters 参数
    * #####  index: number
####  Returns 返回值 ICell
  * com.aspose.cells.Cell get(int, int)
#### Parameters 参数
    * #####  row: number
    * #####  column: number
####  Returns 返回值 ICell


###  getCell 
  * getCell(rownumber, columnnumber)ICell


  * com.aspose.cells.Cell getCell(int, int)
#### Parameters 参数
    * #####  row: number
    * #####  column: number
####  Returns 返回值 ICell


###  getCellStyle 
  * getCellStyle(rownumber, columnnumber)IStyle


  * com.aspose.cells.Style getCellStyle(int, int)
#### Parameters 参数
    * #####  row: number
    * #####  column: number
####  Returns 返回值 IStyle


###  getColumn 
  * getColumn(columnIndexnumber)IColumn


  * com.aspose.cells.Column getColumn(int)
#### Parameters 参数
    * #####  columnIndex: number
####  Returns 返回值 IColumn


###  getColumnWidth 
  * getColumnWidth(columnnumber)number


  * double getColumnWidth(int)
#### Parameters 参数
    * #####  column: number
####  Returns 返回值 number


###  getColumnWidthInch 
  * getColumnWidthInch(columnnumber)number


  * double getColumnWidthInch(int)
#### Parameters 参数
    * #####  column: number
####  Returns 返回值 number


###  getColumnWidthPixel 
  * getColumnWidthPixel(columnnumber)number


  * int getColumnWidthPixel(int)
#### Parameters 参数
    * #####  column: number
####  Returns 返回值 number


###  getColumns 
  * getColumns()IColumnCollection


  * com.aspose.cells.ColumnCollection getColumns()
####  Returns 返回值 IColumnCollection


###  getCount 
  * getCount()number


  * int getCount()
####  Returns 返回值 number


###  getCountLarge 
  * getCountLarge()number


  * long getCountLarge()
####  Returns 返回值 number


###  getDependents 
  * getDependents(isAllboolean, rownumber, columnnumber)ICell[]


  * com.aspose.cells.Cell[] getDependents(boolean, int, int)
#### Parameters 参数
    * #####  isAll: boolean
    * #####  row: number
    * #####  column: number
####  Returns 返回值 ICell[]


###  getFirstCell 
  * getFirst


  * com.aspose.cells.Cell getFirstCell()
####  Returns 返回值 ICell


###  getGroupedColumnOutlineLevel 
  * getGroupedColumnOutlineLevel(columnIndexnumber)number


  * int getGroupedColumnOutlineLevel(int)
#### Parameters 参数
    * #####  columnIndex: number
####  Returns 返回值 number


###  getGroupedRowOutlineLevel 
  * getGroupedRowOutlineLevel(rowIndexnumber)number


  * int getGroupedRowOutlineLevel(int)
#### Parameters 参数
    * #####  rowIndex: number
####  Returns 返回值 number


###  getLastCell 
  * getLast


  * com.aspose.cells.Cell getLastCell()
####  Returns 返回值 ICell


###  getLastData
  * getLastDataRow(columnnumber)number


  * int getLastDataRow(int)
#### Parameters 参数
    * #####  column: number
####  Returns 返回值 number


###  getMaxColumn 
  * getMaxColumn()number


  * int getMaxColumn()
####  Returns 返回值 number


###  getMaxDataColumn 
  * getMaxDataColumn()number


  * int getMaxDataColumn()
####  Returns 返回值 number


###  getMaxData
  * getMaxDataRow()number


  * int getMaxDataRow()
####  Returns 返回值 number


###  getMaxDisplayRange 
  * getMaxDisplay


  * com.aspose.cells.Range getMaxDisplayRange()
####  Returns 返回值 IRange


###  getMaxGroupedColumnOutlineLevel 
  * getMaxGroupedColumnOutlineLevel()number


  * int getMaxGroupedColumnOutlineLevel()
####  Returns 返回值 number


###  getMaxGroupedRowOutlineLevel 
  * getMaxGroupedRowOutlineLevel()number


  * int getMaxGroupedRowOutlineLevel()
####  Returns 返回值 number


###  get 
  * getMaxRow()number


  * int getMaxRow()
####  Returns 返回值 number


###  getMemorySetting 
  * getMemorySetting()number


  * int getMemorySetting()
####  Returns 返回值 number


###  getMergedCells 
  * getMergedCells()object[]


  * java.util.ArrayList getMergedCells()
####  Returns 返回值 object[]


###  getMinColumn 
  * getMinColumn()number


  * int getMinColumn()
####  Returns 返回值 number


###  getMinDataColumn 
  * getMinDataColumn()number


  * int getMinDataColumn()
####  Returns 返回值 number


###  getMinData
  * getMinDataRow()number


  * int getMinDataRow()
####  Returns 返回值 number


###  get 
  * getMinRow()number


  * int getMinRow()
####  Returns 返回值 number


###  getMultiThreadReading 
  * getMultiThreadReading()boolean


  * boolean getMultiThreadReading()
####  Returns 返回值 boolean


###  getOdsCellFields 
  * getOdsCellFields()IOdsCellFieldCollection


  * com.aspose.cells.OdsCellFieldCollection getOdsCellFields()
####  Returns 返回值 IOdsCellFieldCollection


###  getPreserveString 
  * getPreserveString()boolean


  * boolean getPreserveString()
####  Returns 返回值 boolean


###  getRanges 
  * get 


  * com.aspose.cells.RangeCollection getRanges()
####  Returns 返回值 IRangeCollection


###  get 
  * getRow(rownumber)IRow


  * com.aspose.cells.Row getRow(int)
#### Parameters 参数
    * #####  row: number
####  Returns 返回值 IRow


###  getRowEnumerator 
  * getRowEnumerator()any


  * java.util.Iterator getRowEnumerator()
####  Returns 返回值 any


###  getRowHeight 
  * getRowHeight(rownumber)number


  * double getRowHeight(int)
#### Parameters 参数
    * #####  row: number
####  Returns 返回值 number


###  getRowHeightInch 
  * getRowHeightInch(rownumber)number


  * double getRowHeightInch(int)
#### Parameters 参数
    * #####  row: number
####  Returns 返回值 number


###  getRowHeightPixel 
  * getRowHeightPixel(rownumber)number


  * int getRowHeightPixel(int)
#### Parameters 参数
    * #####  row: number
####  Returns 返回值 number


###  getRows 
  * get 


  * com.aspose.cells.RowCollection getRows()
####  Returns 返回值 IRowCollection


###  getStandardHeight 
  * getStandardHeight()number


  * double getStandardHeight()
####  Returns 返回值 number


###  getStandardHeightPixels 
  * getStandardHeightPixels()number


  * int getStandardHeightPixels()
####  Returns 返回值 number


###  getStandardWidth 
  * getStandardWidth()number


  * double getStandardWidth()
####  Returns 返回值 number


###  getStandardWidthInch 
  * getStandardWidthInch()number


  * double getStandardWidthInch()
####  Returns 返回值 number


###  getStandardWidthPixels 
  * getStandardWidthPixels()number


  * int getStandardWidthPixels()
####  Returns 返回值 number


###  getStyle 
  * get 


  * com.aspose.cells.Style getStyle()
####  Returns 返回值 IStyle


###  getViewColumnWidthPixel 
  * getViewColumnWidthPixel(columnnumber)number


  * int getViewColumnWidthPixel(int)
#### Parameters 参数
    * #####  column: number
####  Returns 返回值 number


###  getViewRowHeight 
  * getViewRowHeight(rownumber)number


  * double getViewRowHeight(int)
#### Parameters 参数
    * #####  row: number
####  Returns 返回值 number


###  getViewRowHeightInch 
  * getViewRowHeightInch(rownumber)number


  * double getViewRowHeightInch(int)
#### Parameters 参数
    * #####  row: number
####  Returns 返回值 number


###  groupColumns 
  * groupColumns(firstIndexnumber, lastIndexnumber)void
  * groupColumns(firstIndexnumber, lastIndexnumber, isHiddenboolean)void


  * void groupColumns(int, int)
#### Parameters 参数
    * #####  firstIndex: number
    * #####  lastIndex: number
####  Returns 返回值 void
  * void groupColumns(int, int, boolean)
#### Parameters 参数
    * #####  firstIndex: number
    * #####  lastIndex: number
    * #####  isHidden: boolean
####  Returns 返回值 void


###  groupRows 
  * groupRows(firstIndexnumber, lastIndexnumber, isHiddenboolean)void
  * groupRows(firstIndexnumber, lastIndexnumber)void


  * void groupRows(int, int, boolean)
#### Parameters 参数
    * #####  firstIndex: number
    * #####  lastIndex: number
    * #####  isHidden: boolean
####  Returns 返回值 void
  * void groupRows(int, int)
#### Parameters 参数
    * #####  firstIndex: number
    * #####  lastIndex: number
####  Returns 返回值 void


###  hideColumn 
  * hideColumn(columnnumber)void


  * void hideColumn(int)
#### Parameters 参数
    * #####  column: number
####  Returns 返回值 void


###  hideColumns 
  * hideColumns(columnnumber, totalColumnsnumber)void


  * void hideColumns(int, int)
#### Parameters 参数
    * #####  column: number
    * #####  totalColumns: number
####  Returns 返回值 void


###  hideGroupDetail 
  * hideGroupDetail(isVerticalboolean, indexnumber)void


  * void hideGroupDetail(boolean, int)
#### Parameters 参数
    * #####  isVertical: boolean
    * #####  index: number
####  Returns 返回值 void


###  hide 
  * hideRow(rownumber)void


  * void hideRow(int)
#### Parameters 参数
    * #####  row: number
####  Returns 返回值 void


###  hideRows 
  * hideRows(rownumber, totalRowsnumber)void


  * void hideRows(int, int)
#### Parameters 参数
    * #####  row: number
    * #####  totalRows: number
####  Returns 返回值 void


###  importArray 
  * importArray(stringArraystring[], firstRownumber, firstColumnnumber, isVerticalboolean)void
  * importArray(stringArraystring[][], firstRownumber, firstColumnnumber)void
  * importArray(doubleArraynumber[][], firstRownumber, firstColumnnumber)void
  * importArray(intArraynumber[], firstRownumber, firstColumnnumber, isVerticalboolean)void
  * importArray(doubleArraynumber[], firstRownumber, firstColumnnumber, isVerticalboolean)void
  * importArray(intArraynumber[][], firstRownumber, firstColumnnumber)void


  * void importArray(java.lang.String[], int, int, boolean)
#### Parameters 参数
    * #####  stringArray: string[]
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  isVertical: boolean
####  Returns 返回值 void
  * void importArray(java.lang.String[][], int, int)
#### Parameters 参数
    * #####  stringArray: string[][]
    * #####  firstRow: number
    * #####  firstColumn: number
####  Returns 返回值 void
  * void importArray(double[][], int, int)
#### Parameters 参数
    * #####  doubleArray: number[][]
    * #####  firstRow: number
    * #####  firstColumn: number
####  Returns 返回值 void
  * void importArray(int[], int, int, boolean)
#### Parameters 参数
    * #####  intArray: number[]
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  isVertical: boolean
####  Returns 返回值 void
  * void importArray(double[], int, int, boolean)
#### Parameters 参数
    * #####  doubleArray: number[]
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  isVertical: boolean
####  Returns 返回值 void
  * void importArray(int[][], int, int)
#### Parameters 参数
    * #####  intArray: number[][]
    * #####  firstRow: number
    * #####  firstColumn: number
####  Returns 返回值 void


###  importArrayList 
  * importArrayList(arrayListobject[], firstRownumber, firstColumnnumber, isVerticalboolean)void


  * void importArrayList(java.util.ArrayList, int, int, boolean)
#### Parameters 参数
    * #####  arrayList: object[]
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  isVertical: boolean
####  Returns 返回值 void


###  importCSV 
  * importCSV(fileNamestring, splitterstring, convertNumericDataboolean, firstRownumber, firstColumnnumber)void
  * importCSV(fileNamestring, optionsITxtLoadOptions, firstRownumber, firstColumnnumber)void
  * importCSV(streamany, optionsITxtLoadOptions, firstRownumber, firstColumnnumber)void
  * importCSV(streamany, splitterstring, convertNumericDataboolean, firstRownumber, firstColumnnumber)void


  * void importCSV(java.lang.String, java.lang.String, boolean, int, int)
#### Parameters 参数
    * #####  fileName: string
    * #####  splitter: string
    * #####  convertNumericData: boolean
    * #####  firstRow: number
    * #####  firstColumn: number
####  Returns 返回值 void
  * void importCSV(java.lang.String, com.aspose.cells.TxtLoadOptions, int, int)
#### Parameters 参数
    * #####  fileName: string
    * #####  options: ITxtLoadOptions
    * #####  firstRow: number
    * #####  firstColumn: number
####  Returns 返回值 void
  * void importCSV(java.io.InputStream, com.aspose.cells.TxtLoadOptions, int, int)
#### Parameters 参数
    * #####  stream: any
    * #####  options: ITxtLoadOptions
    * #####  firstRow: number
    * #####  firstColumn: number
####  Returns 返回值 void
  * void importCSV(java.io.InputStream, java.lang.String, boolean, int, int)
#### Parameters 参数
    * #####  stream: any
    * #####  splitter: string
    * #####  convertNumericData: boolean
    * #####  firstRow: number
    * #####  firstColumn: number
####  Returns 返回值 void


###  importCustomObjects 
  * importCustomObjects(listobject[], firstRownumber, firstColumnnumber, optionsIImportTableOptions)number
  * importCustomObjects(listobject[], propertyNamesstring[], isPropertyNameShownboolean, firstRownumber, firstColumnnumber, rowNumbernumber, insertRowsboolean, dateFormatStringstring, convertStringToNumberboolean)number


  * int importCustomObjects(java.util.Collection, int, int, com.aspose.cells.ImportTableOptions)
#### Parameters 参数
    * #####  list: object[]
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  options: IImportTableOptions
####  Returns 返回值 number
  * int importCustomObjects(java.util.Collection, java.lang.String[], boolean, int, int, int, boolean, java.lang.String, boolean)
#### Parameters 参数
    * #####  list: object[]
    * #####  propertyNames: string[]
    * #####  isPropertyNameShown: boolean
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  rowNumber: number
    * #####  insertRows: boolean
    * #####  dateFormatString: string
    * #####  convertStringToNumber: boolean
####  Returns 返回值 number


###  importData 
  * importData(tableIICellsDataTable, firstRownumber, firstColumnnumber, optionsIImportTableOptions)number


  * int importData(com.aspose.cells.ICellsDataTable, int, int, com.aspose.cells.ImportTableOptions)
#### Parameters 参数
    * #####  table: IICellsDataTable
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  options: IImportTableOptions
####  Returns 返回值 number


###  importFormulaArray 
  * importFormulaArray(stringArraystring[], firstRownumber, firstColumnnumber, isVerticalboolean)void


  * void importFormulaArray(java.lang.String[], int, int, boolean)
#### Parameters 参数
    * #####  stringArray: string[]
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  isVertical: boolean
####  Returns 返回值 void


###  importObjectArray 
  * importObjectArray(objArrayany[], firstRownumber, firstColumnnumber, isVerticalboolean)void
  * importObjectArray(objArrayany[], firstRownumber, firstColumnnumber, isVerticalboolean, skipnumber)void


  * void importObjectArray(java.lang.Object[], int, int, boolean)
#### Parameters 参数
    * #####  objArray: any[]
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  isVertical: boolean
####  Returns 返回值 void
  * void importObjectArray(java.lang.Object[], int, int, boolean, int)
#### Parameters 参数
    * #####  objArray: any[]
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  isVertical: boolean
    * #####  skip: number
####  Returns 返回值 void


###  importResult
  * importResultSet(rsany, rowIndexnumber, columnIndexnumber, optionsIImportTableOptions)number
  * importResultSet(rsany, rowIndexnumber, columnIndexnumber, rowNumnumber, columnNumnumber, isFieldNameShownboolean, customDateFormatStringstring, convertStringToNumberboolean)number
  * importResultSet(rsany, startCellstring, optionsIImportTableOptions)number
  * importResultSet(rsany, startCellstring, rowNumnumber, columnNumnumber, isFieldNameShownboolean)number
  * importResultSet(rsany, rowIndexnumber, columnIndexnumber, isFieldNameShownboolean)number
  * importResultSet(rsany, rowIndexnumber, columnIndexnumber, rowNumnumber, columnNumnumber, isFieldNameShownboolean)number
  * importResultSet(rsany, startCellstring, isFieldNameShownboolean)number
  * importResultSet(rsany, rowIndexnumber, columnIndexnumber, isFieldNameShownboolean, customDateFormatStringstring, convertStringToNumberboolean)number


  * int importResultSet(java.sql.ResultSet, int, int, com.aspose.cells.ImportTableOptions)
#### Parameters 参数
    * #####  rowIndex: number
    * #####  columnIndex: number
    * #####  options: IImportTableOptions
####  Returns 返回值 number
  * int importResultSet(java.sql.ResultSet, int, int, int, int, boolean, java.lang.String, boolean)
#### Parameters 参数
    * #####  rowIndex: number
    * #####  columnIndex: number
    * #####  rowNum: number
    * #####  columnNum: number
    * #####  isFieldNameShown: boolean
    * #####  customDateFormatString: string
    * #####  convertStringToNumber: boolean
####  Returns 返回值 number
  * int importResultSet(java.sql.ResultSet, java.lang.String, com.aspose.cells.ImportTableOptions)
#### Parameters 参数
    * #####  startCell: string
    * #####  options: IImportTableOptions
####  Returns 返回值 number
  * int importResultSet(java.sql.ResultSet, java.lang.String, int, int, boolean)
#### Parameters 参数
    * #####  startCell: string
    * #####  rowNum: number
    * #####  columnNum: number
    * #####  isFieldNameShown: boolean
####  Returns 返回值 number
  * int importResultSet(java.sql.ResultSet, int, int, boolean)
#### Parameters 参数
    * #####  rowIndex: number
    * #####  columnIndex: number
    * #####  isFieldNameShown: boolean
####  Returns 返回值 number
  * int importResultSet(java.sql.ResultSet, int, int, int, int, boolean)
#### Parameters 参数
    * #####  rowIndex: number
    * #####  columnIndex: number
    * #####  rowNum: number
    * #####  columnNum: number
    * #####  isFieldNameShown: boolean
####  Returns 返回值 number
  * int importResultSet(java.sql.ResultSet, java.lang.String, boolean)
#### Parameters 参数
    * #####  startCell: string
    * #####  isFieldNameShown: boolean
####  Returns 返回值 number
  * int importResultSet(java.sql.ResultSet, int, int, boolean, java.lang.String, boolean)
#### Parameters 参数
    * #####  rowIndex: number
    * #####  columnIndex: number
    * #####  isFieldNameShown: boolean
    * #####  customDateFormatString: string
    * #####  convertStringToNumber: boolean
####  Returns 返回值 number


###  importTwoDimensionArray 
  * importTwoDimensionArray(objArrayany[][], firstRownumber, firstColumnnumber)void
  * importTwoDimensionArray(objArrayany[][], firstRownumber, firstColumnnumber, convertStringToNumberboolean)void
  * importTwoDimensionArray(objArrayany[][], stylesany[][], firstRownumber, firstColumnnumber, optsITxtLoadOptions)void
  * importTwoDimensionArray(objArrayany[][], stylesany[][], firstRownumber, firstColumnnumber, convertStringToNumberboolean)void


  * void importTwoDimensionArray(java.lang.Object[][], int, int)
#### Parameters 参数
    * #####  objArray: any[][]
    * #####  firstRow: number
    * #####  firstColumn: number
####  Returns 返回值 void
  * void importTwoDimensionArray(java.lang.Object[][], int, int, boolean)
#### Parameters 参数
    * #####  objArray: any[][]
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  convertStringToNumber: boolean
####  Returns 返回值 void
  * void importTwoDimensionArray(java.lang.Object[][], java.lang.Object[][], int, int, com.aspose.cells.TxtLoadOptions)
#### Parameters 参数
    * #####  objArray: any[][]
    * #####  styles: any[][]
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  opts: ITxtLoadOptions
####  Returns 返回值 void
  * void importTwoDimensionArray(java.lang.Object[][], java.lang.Object[][], int, int, boolean)
#### Parameters 参数
    * #####  objArray: any[][]
    * #####  styles: any[][]
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  convertStringToNumber: boolean
####  Returns 返回值 void


###  insertColumn 
  * insertColumn(columnIndexnumber, updateReferenceboolean)void
  * insertColumn(columnIndexnumber)void


  * void insertColumn(int, boolean)
#### Parameters 参数
    * #####  columnIndex: number
    * #####  updateReference: boolean
####  Returns 返回值 void
  * void insertColumn(int)
#### Parameters 参数
    * #####  columnIndex: number
####  Returns 返回值 void


###  insertColumns 
  * insertColumns(columnIndexnumber, totalColumnsnumber)void
  * insertColumns(columnIndexnumber, totalColumnsnumber, updateReferenceboolean)void


  * void insertColumns(int, int)
#### Parameters 参数
    * #####  columnIndex: number
    * #####  totalColumns: number
####  Returns 返回值 void
  * void insertColumns(int, int, boolean)
#### Parameters 参数
    * #####  columnIndex: number
    * #####  totalColumns: number
    * #####  updateReference: boolean
####  Returns 返回值 void


###  insertCutCells 
  * insertCutCells(cutRangeIRange, rownumber, columnnumber, shiftTypenumber)void


  * void insertCutCells(com.aspose.cells.Range, int, int, int)
#### Parameters 参数
    * #####  cutRange: IRange
    * #####  row: number
    * #####  column: number
    * #####  shiftType: number
####  Returns 返回值 void


###  insertRange 
  * insertRange(areaICellArea, shiftNumbernumber, shiftTypenumber, updateReferenceboolean)void
  * insertRange(areaICellArea, shiftTypenumber)void
  * insertRange(areaICellArea, shiftNumbernumber, shiftTypenumber)void


  * void insertRange(com.aspose.cells.CellArea, int, int, boolean)
#### Parameters 参数
    *     * #####  shiftNumber: number
    * #####  shiftType: number
    * #####  updateReference: boolean
####  Returns 返回值 void
  * void insertRange(com.aspose.cells.CellArea, int)
#### Parameters 参数
    *     * #####  shiftType: number
####  Returns 返回值 void
  * void insertRange(com.aspose.cells.CellArea, int, int)
#### Parameters 参数
    *     * #####  shiftNumber: number
    * #####  shiftType: number
####  Returns 返回值 void


###  insert 
  * insertRow(rowIndexnumber)void


  * void insertRow(int)
#### Parameters 参数
    * #####  rowIndex: number
####  Returns 返回值 void


###  insertRows 
  * insertRows(rowIndexnumber, totalRowsnumber, optionsIInsertOptions)void
  * insertRows(rowIndexnumber, totalRowsnumber)void
  * insertRows(rowIndexnumber, totalRowsnumber, updateReferenceboolean)void


  * void insertRows(int, int, com.aspose.cells.InsertOptions)
#### Parameters 参数
    * #####  rowIndex: number
    * #####  totalRows: number
    * #####  options: IInsertOptions
####  Returns 返回值 void
  * void insertRows(int, int)
#### Parameters 参数
    * #####  rowIndex: number
    * #####  totalRows: number
####  Returns 返回值 void
  * void insertRows(int, int, boolean)
#### Parameters 参数
    * #####  rowIndex: number
    * #####  totalRows: number
    * #####  updateReference: boolean
####  Returns 返回值 void


###  isBlankColumn 
  * isBlankColumn(columnIndexnumber)boolean


  * boolean isBlankColumn(int)
#### Parameters 参数
    * #####  columnIndex: number
####  Returns 返回值 boolean


###  isColumnHidden 
  * isColumnHidden(columnIndexnumber)boolean


  * boolean isColumnHidden(int)
#### Parameters 参数
    * #####  columnIndex: number
####  Returns 返回值 boolean


###  isDefaultRowHeightMatched 
  * isDefaultRowHeightMatched()boolean


  * boolean isDefaultRowHeightMatched()
####  Returns 返回值 boolean


###  isDefaultRowHidden 
  * isDefaultRowHidden()boolean


  * boolean isDefaultRowHidden()
####  Returns 返回值 boolean


###  isDeletingRangeEnabled 
  * isDeletingRangeEnabled(startRownumber, startColumnnumber, totalRowsnumber, totalColumnsnumber)boolean


  * boolean isDeletingRangeEnabled(int, int, int, int)
#### Parameters 参数
    * #####  startRow: number
    * #####  startColumn: number
    * #####  totalRows: number
    * #####  totalColumns: number
####  Returns 返回值 boolean


###  isRowHidden 
  * isRowHidden(rowIndexnumber)boolean


  * boolean isRowHidden(int)
#### Parameters 参数
    * #####  rowIndex: number
####  Returns 返回值 boolean


###  iterator 
  * iterator()any


  * java.util.Iterator iterator()
####  Returns 返回值 any


###  linkToXml
  * linkToXmlMap(mapNamestring, rownumber, columnnumber, pathstring)void


  * void linkToXmlMap(java.lang.String, int, int, java.lang.String)
#### Parameters 参数
    * #####  mapName: string
    * #####  row: number
    * #####  column: number
    * #####  path: string
####  Returns 返回值 void


###  merge 
  * merge(firstRownumber, firstColumnnumber, totalRowsnumber, totalColumnsnumber, mergeConflictboolean)void
  * merge(firstRownumber, firstColumnnumber, totalRowsnumber, totalColumnsnumber, checkConflictboolean, mergeConflictboolean)void
  * merge(firstRownumber, firstColumnnumber, totalRowsnumber, totalColumnsnumber)void


  * void merge(int, int, int, int, boolean)
#### Parameters 参数
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  totalRows: number
    * #####  totalColumns: number
    * #####  mergeConflict: boolean
####  Returns 返回值 void
  * void merge(int, int, int, int, boolean, boolean)
#### Parameters 参数
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  totalRows: number
    * #####  totalColumns: number
    * #####  checkConflict: boolean
    * #####  mergeConflict: boolean
####  Returns 返回值 void
  * void merge(int, int, int, int)
#### Parameters 参数
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  totalRows: number
    * #####  totalColumns: number
####  Returns 返回值 void


###  moveRange 
  * moveRange(sourceAreaICellArea, destRownumber, destColumnnumber)void


  * void moveRange(com.aspose.cells.CellArea, int, int)
#### Parameters 参数
    * #####  sourceArea: ICellArea
    * #####  destRow: number
    * #####  destColumn: number
####  Returns 返回值 void


###  removeDuplicates 
  * removeDuplicates()void
  * removeDuplicates(startRownumber, startColumnnumber, endRownumber, endColumnnumber)void
  * removeDuplicates(startRownumber, startColumnnumber, endRownumber, endColumnnumber, hasHeadersboolean, columnOffsetsnumber[])void


  * void removeDuplicates()
####  Returns 返回值 void
  * void removeDuplicates(int, int, int, int)
#### Parameters 参数
    * #####  startRow: number
    * #####  startColumn: number
    * #####  endRow: number
    * #####  endColumn: number
####  Returns 返回值 void
  * void removeDuplicates(int, int, int, int, boolean, int[])
#### Parameters 参数
    * #####  startRow: number
    * #####  startColumn: number
    * #####  endRow: number
    * #####  endColumn: number
    * #####  hasHeaders: boolean
    * #####  columnOffsets: number[]
####  Returns 返回值 void


###  removeFormulas 
  * removeFormulas()void


  * void removeFormulas()
####  Returns 返回值 void


###  retrieveSubtotalSetting 
  * retrieveSubtotalSetting(caICellArea)ISubtotalSetting


  * com.aspose.cells.SubtotalSetting retrieveSubtotalSetting(com.aspose.cells.CellArea)
#### Parameters 参数
    * ####  Returns 返回值 ISubtotalSetting


###  setColumnWidth 
  * setColumnWidth(columnnumber, widthnumber)void


  * void setColumnWidth(int, double)
#### Parameters 参数
    * #####  column: number
    * #####  width: number
####  Returns 返回值 void


###  setColumnWidthInch 
  * setColumnWidthInch(columnnumber, inchesnumber)void


  * void setColumnWidthInch(int, double)
#### Parameters 参数
    * #####  column: number
    * #####  inches: number
####  Returns 返回值 void


###  setColumnWidthPixel 
  * setColumnWidthPixel(columnnumber, pixelsnumber)void


  * void setColumnWidthPixel(int, int)
#### Parameters 参数
    * #####  column: number
    * #####  pixels: number
####  Returns 返回值 void


###  setDefaultRowHeightMatched 
  * setDefaultRowHeightMatched(valueboolean)void


  * void setDefaultRowHeightMatched(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setDefaultRowHidden 
  * setDefaultRowHidden(valueboolean)void


  * void setDefaultRowHidden(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setMemorySetting 
  * setMemorySetting(valuenumber)void


  * void setMemorySetting(int)
#### Parameters 参数
    * #####  value: number
####  Returns 返回值 void


###  setMultiThreadReading 
  * setMultiThreadReading(valueboolean)void


  * void setMultiThreadReading(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setPreserveString 
  * setPreserveString(valueboolean)void


  * void setPreserveString(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setRowHeight 
  * setRowHeight(rownumber, heightnumber)void


  * void setRowHeight(int, double)
#### Parameters 参数
    * #####  row: number
    * #####  height: number
####  Returns 返回值 void


###  setRowHeightInch 
  * setRowHeightInch(rownumber, inchesnumber)void


  * void setRowHeightInch(int, double)
#### Parameters 参数
    * #####  row: number
    * #####  inches: number
####  Returns 返回值 void


###  setRowHeightPixel 
  * setRowHeightPixel(rownumber, pixelsnumber)void


  * void setRowHeightPixel(int, int)
#### Parameters 参数
    * #####  row: number
    * #####  pixels: number
####  Returns 返回值 void


###  setStandardHeight 
  * setStandardHeight(valuenumber)void


  * void setStandardHeight(double)
#### Parameters 参数
    * #####  value: number
####  Returns 返回值 void


###  setStandardHeightPixels 
  * setStandardHeightPixels(valuenumber)void


  * void setStandardHeightPixels(int)
#### Parameters 参数
    * #####  value: number
####  Returns 返回值 void


###  setStandardWidth 
  * setStandardWidth(valuenumber)void


  * void setStandardWidth(double)
#### Parameters 参数
    * #####  value: number
####  Returns 返回值 void


###  setStandardWidthInch 
  * setStandardWidthInch(valuenumber)void


  * void setStandardWidthInch(double)
#### Parameters 参数
    * #####  value: number
####  Returns 返回值 void


###  setStandardWidthPixels 
  * setStandardWidthPixels(valuenumber)void


  * void setStandardWidthPixels(int)
#### Parameters 参数
    * #####  value: number
####  Returns 返回值 void


###  setStyle 
  * setStyle(valueIStyle)void


  * void setStyle(com.aspose.cells.Style)
#### Parameters 参数
    * #####  value: IStyle
####  Returns 返回值 void


###  setViewColumnWidthPixel 
  * setViewColumnWidthPixel(columnnumber, pixelsnumber)void


  * void setViewColumnWidthPixel(int, int)
#### Parameters 参数
    * #####  column: number
    * #####  pixels: number
####  Returns 返回值 void


###  showGroupDetail 
  * showGroupDetail(isVerticalboolean, indexnumber)void


  * void showGroupDetail(boolean, int)
#### Parameters 参数
    * #####  isVertical: boolean
    * #####  index: number
####  Returns 返回值 void


###  subtotal 
  * subtotal(caICellArea, groupBynumber, fnnumber, totalListnumber[])void
  * subtotal(caICellArea, groupBynumber, fnnumber, totalListnumber[], replaceboolean, pageBreaksboolean, summaryBelowDataboolean)void


  * void subtotal(com.aspose.cells.CellArea, int, int, int[])
#### Parameters 参数
    *     * #####  groupBy: number
    * #####  fn: number
    * #####  totalList: number[]
####  Returns 返回值 void
  * void subtotal(com.aspose.cells.CellArea, int, int, int[], boolean, boolean, boolean)
#### Parameters 参数
    *     * #####  groupBy: number
    * #####  fn: number
    * #####  totalList: number[]
    * #####  replace: boolean
    * #####  pageBreaks: boolean
    * #####  summaryBelowData: boolean
####  Returns 返回值 void


###  textToColumns 
  * textToColumns(rownumber, columnnumber, totalRowsnumber, optionsITxtLoadOptions)void


  * void textToColumns(int, int, int, com.aspose.cells.TxtLoadOptions)
#### Parameters 参数
    * #####  row: number
    * #####  column: number
    * #####  totalRows: number
    * #####  options: ITxtLoadOptions
####  Returns 返回值 void


###  unMerge 
  * unMerge(firstRownumber, firstColumnnumber, totalRowsnumber, totalColumnsnumber)void


  * void unMerge(int, int, int, int)
#### Parameters 参数
    * #####  firstRow: number
    * #####  firstColumn: number
    * #####  totalRows: number
    * #####  totalColumns: number
####  Returns 返回值 void


###  ungroupColumns 
  * ungroupColumns(firstIndexnumber, lastIndexnumber)void


  * void ungroupColumns(int, int)
#### Parameters 参数
    * #####  firstIndex: number
    * #####  lastIndex: number
####  Returns 返回值 void


###  ungroupRows 
  * ungroupRows(firstIndexnumber, lastIndexnumber)void
  * ungroupRows(firstIndexnumber, lastIndexnumber, isAllboolean)void


  * void ungroupRows(int, int)
#### Parameters 参数
    * #####  firstIndex: number
    * #####  lastIndex: number
####  Returns 返回值 void
  * void ungroupRows(int, int, boolean)
#### Parameters 参数
    * #####  firstIndex: number
    * #####  lastIndex: number
    * #####  isAll: boolean
####  Returns 返回值 void


###  unhideColumn 
  * unhideColumn(columnnumber, widthnumber)void


  * void unhideColumn(int, double)
#### Parameters 参数
    * #####  column: number
    * #####  width: number
####  Returns 返回值 void


###  unhideColumns 
  * unhideColumns(columnnumber, totalColumnsnumber, widthnumber)void


  * void unhideColumns(int, int, double)
#### Parameters 参数
    * #####  column: number
    * #####  totalColumns: number
    * #####  width: number
####  Returns 返回值 void


###  unhide 
  * unhideRow(rownumber, heightnumber)void


  * void unhideRow(int, double)
#### Parameters 参数
    * #####  row: number
    * #####  height: number
####  Returns 返回值 void


###  unhideRows 
  * unhideRows(rownumber, totalRowsnumber, heightnumber)void


  * void unhideRows(int, int, double)
#### Parameters 参数
    * #####  row: number
    * #####  totalRows: number
    * #####  height: number
####  Returns 返回值 void



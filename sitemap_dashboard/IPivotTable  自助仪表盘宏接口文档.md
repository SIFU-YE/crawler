com.aspose.cells.PivotTable
### Hierarchy 层级


## Index 目录
###  Methods 方法 
  * addCalculatedField
  * addFieldToArea
  * calculateData
  * calculateRange
  * changeDataSource
  * getAltTextDescription
  * getAltTextTitle
  * getAutoFormatType
  * getBaseFields
  * getCellByDisplayName
  * getChildren
  * getColumnFields
  * getColumnGrand
  * getColumnHeaderCaption
  * getColumnRange
  * getCustomListSort
  * getDataBodyRange
  * getDataField
  * getDataFields
  * getDataSource
  * getDisplayErrorString
  * getDisplayImmediateItems
  * getDisplayNullString
  * getEnableDataValueEditing
  * getEnableDrilldown
  * getEnableFieldDialog
  * getEnableFieldList
  * getEnableWizard
  * getErrorString
  * getExternalConnectionDataSource
  * getFieldListSortAscending
  * getGrandTotalName
  * getHorizontalBreaks
  * getItemPrintTitles
  * getManualUpdate
  * getMergeLabels
  * getMissingItemsLimit
  * getNullString
  * getPageFieldOrder
  * getPageFieldWrapCount
  * getPageFields
  * getPivotFilters
  * getPivotFormatConditions
  * getPivotTableStyleName
  * getPivotTableStyleType
  * getPreserveFormatting
  * getPrintDrill
  * getPrintTitles
  * getRefreshDataFlag
  * getRefreshDataOnOpeningFile
  * getRefreshDate
  * getRefreshedByWho
  * getRowFields
  * getRowGrand
  * getRowHeaderCaption
  * getRowRange
  * getSaveData
  * getShowDataTips
  * getShowDrill
  * getShowEmptyCol
  * getShowEmptyRow
  * getShowMemberPropertyTips
  * getShowPivotStyleColumnHeader
  * getShowPivotStyleColumnStripes
  * getShowPivotStyleLastColumn
  * getShowPivotStyleRowHeader
  * getShowPivotStyleRowStripes
  * getShowRowHeaderCaption
  * getShowValuesRow
  * getSubtotalHiddenPageItems
  * getTableRange1
  * getTableRange2
  * hasBlankRows
  * isAutoFormat
  * isExcel2003Compatible
  * isGridDropZones
  * isMultipleFieldFilters
  * refreshData
  * removeField
  * setAltTextDescription
  * setAltTextTitle
  * setAutoFormat
  * setAutoFormatType
  * setAutoGroupField
  * setColumnGrand
  * setColumnHeaderCaption
  * setCustomListSort
  * setDataSource
  * setDisplayErrorString
  * setDisplayImmediateItems
  * setDisplayNullString
  * setEnableDataValueEditing
  * setEnableDrilldown
  * setEnableFieldDialog
  * setEnableFieldList
  * setEnableWizard
  * setErrorString
  * setExcel2003Compatible
  * setFieldListSortAscending
  * setGrandTotalName
  * setGridDropZones
  * setHasBlankRows
  * setItemPrintTitles
  * setManualGroupField
  * setManualUpdate
  * setMergeLabels
  * setMissingItemsLimit
  * setMultipleFieldFilters
  * setNullString
  * setPageFieldOrder
  * setPageFieldWrapCount
  * setPivotTableStyleName
  * setPivotTableStyleType
  * setPreserveFormatting
  * setPrintDrill
  * setPrintTitles
  * setRefreshDataFlag
  * setRefreshDataOnOpeningFile
  * setRowGrand
  * setRowHeaderCaption
  * setSaveData
  * setSelected
  * setShowDataTips
  * setShowDrill
  * setShowEmptyCol
  * setShowEmptyRow
  * setShowMemberPropertyTips
  * setShowPivotStyleColumnHeader
  * setShowPivotStyleColumnStripes
  * setShowPivotStyleLastColumn
  * setShowPivotStyleRowHeader
  * setShowPivotStyleRowStripes
  * setShowRowHeaderCaption
  * setShowValuesRow
  * setSubtotalHiddenPageItems
  * showInCompactForm
  * showInOutlineForm
  * showInTabularForm
  * showReportFilterPage
  * showReportFilterPageByIndex
  * showReportFilterPageByName


##  Methods 方法 
###  addCalculatedField 
  * addCalculatedField(namestring, formulastring)void
  * addCalculatedField(namestring, formulastring, dragToDataAreaboolean)void


  * void addCalculatedField(java.lang.String, java.lang.String)
#### Parameters 参数
    * #####  name: string
    * #####  formula: string
####  Returns 返回值 void
  * void addCalculatedField(java.lang.String, java.lang.String, boolean)
#### Parameters 参数
    * #####  name: string
    * #####  formula: string
    * #####  dragToDataArea: boolean
####  Returns 返回值 void


###  addFieldToArea 
  * addFieldToArea(fieldTypenumber, fieldNamestring)number
  * addFieldToArea(fieldTypenumber, pivotFieldIPivotField)number
  * addFieldToArea(fieldTypenumber, baseFieldIndexnumber)number


  * int addFieldToArea(int, java.lang.String)
#### Parameters 参数
    * #####  fieldType: number
    * #####  fieldName: string
####  Returns 返回值 number
  * int addFieldToArea(int, com.aspose.cells.PivotField)
#### Parameters 参数
    * #####  fieldType: number
    * #####  pivotField: IPivotField
####  Returns 返回值 number
  * int addFieldToArea(int, int)
#### Parameters 参数
    * #####  fieldType: number
    * #####  baseFieldIndex: number
####  Returns 返回值 number


###  calculateData 
  * calculateData()void


  * void calculateData()
####  Returns 返回值 void


###  calculateRange 
  * calculateRange()void


  * void calculateRange()
####  Returns 返回值 void


###  changeDataSource 
  * changeDataSource(sourcestring[])void


  * void changeDataSource(java.lang.String[])
#### Parameters 参数
    * #####  source: string[]
####  Returns 返回值 void


###  clearData 
  * clearData()void


  * void clearData()
####  Returns 返回值 void


###  copyStyle 
  * copyStyle(pivotTableIPivotTable)void


  * void copyStyle(com.aspose.cells.PivotTable)
#### Parameters 参数
    * #####  pivotTable: IPivotTable
####  Returns 返回值 void


###  dispose 
  * dispose()void


  * void dispose()
####  Returns 返回值 void


###  fields 
  * fields(fieldTypenumber)IPivotFieldCollection


  * com.aspose.cells.PivotFieldCollection fields(int)
#### Parameters 参数
    * #####  fieldType: number
####  Returns 返回值 IPivotFieldCollection


###  format 
  * format(rownumber, columnnumber, styleIStyle)void


  * void format(int, int, com.aspose.cells.Style)
#### Parameters 参数
    * #####  row: number
    * #####  column: number
    * #####  style: IStyle
####  Returns 返回值 void


###  format 
  * formatAll(styleIStyle)void


  * void formatAll(com.aspose.cells.Style)
#### Parameters 参数
    * #####  style: IStyle
####  Returns 返回值 void


###  getAltTextDescription 
  * getAltTextDescription()string


  * java.lang.String getAltTextDescription()
####  Returns 返回值 string


###  getAltTextTitle 
  * getAltTextTitle()string


  * java.lang.String getAltTextTitle()
####  Returns 返回值 string


###  getAutoFormatType 
  * getAutoFormatType()number


  * int getAutoFormatType()
####  Returns 返回值 number


###  getBaseFields 
  * getBaseFields()IPivotFieldCollection


  * com.aspose.cells.PivotFieldCollection getBaseFields()
####  Returns 返回值 IPivotFieldCollection


###  getCellByDisplayName 
  * getCellByDisplayName(displayNamestring)ICell


  * com.aspose.cells.Cell getCellByDisplayName(java.lang.String)
#### Parameters 参数
    * #####  displayName: string
####  Returns 返回值 ICell


###  getChildren 
  * getChildren()IPivotTable[]


  * com.aspose.cells.PivotTable[] getChildren()
####  Returns 返回值 IPivotTable[]


###  getColumnFields 
  * getColumnFields()IPivotFieldCollection


  * com.aspose.cells.PivotFieldCollection getColumnFields()
####  Returns 返回值 IPivotFieldCollection


###  getColumnGrand 
  * getColumnGrand()boolean


  * boolean getColumnGrand()
####  Returns 返回值 boolean


###  getColumnHeaderCaption 
  * getColumnHeaderCaption()string


  * java.lang.String getColumnHeaderCaption()
####  Returns 返回值 string


###  getColumnRange 
  * getColumn


  * com.aspose.cells.CellArea getColumnRange()
####  Returns 返回值 ICellArea


###  getCustomListSort 
  * getCustomListSort()boolean


  * boolean getCustomListSort()
####  Returns 返回值 boolean


###  getDataBodyRange 
  * getDataBody


  * com.aspose.cells.CellArea getDataBodyRange()
####  Returns 返回值 ICellArea


###  getDataField 
  * getData


  * com.aspose.cells.PivotField getDataField()
####  Returns 返回值 IPivotField


###  getDataFields 
  * getDataFields()IPivotFieldCollection


  * com.aspose.cells.PivotFieldCollection getDataFields()
####  Returns 返回值 IPivotFieldCollection


###  getDataSource 
  * getDataSource()string[]


  * java.lang.String[] getDataSource()
####  Returns 返回值 string[]


###  getDisplayErrorString 
  * getDisplayErrorString()boolean


  * boolean getDisplayErrorString()
####  Returns 返回值 boolean


###  getDisplayImmediateItems 
  * getDisplayImmediateItems()boolean


  * boolean getDisplayImmediateItems()
####  Returns 返回值 boolean


###  getDisplayNullString 
  * getDisplayNullString()boolean


  * boolean getDisplayNullString()
####  Returns 返回值 boolean


###  getEnableDataValueEditing 
  * getEnableDataValueEditing()boolean


  * boolean getEnableDataValueEditing()
####  Returns 返回值 boolean


###  getEnableDrilldown 
  * getEnableDrilldown()boolean


  * boolean getEnableDrilldown()
####  Returns 返回值 boolean


###  getEnableFieldDialog 
  * getEnableFieldDialog()boolean


  * boolean getEnableFieldDialog()
####  Returns 返回值 boolean


###  getEnableFieldList 
  * getEnableFieldList()boolean


  * boolean getEnableFieldList()
####  Returns 返回值 boolean


###  getEnableWizard 
  * getEnableWizard()boolean


  * boolean getEnableWizard()
####  Returns 返回值 boolean


###  getErrorString 
  * getErrorString()string


  * java.lang.String getErrorString()
####  Returns 返回值 string


###  getExternalConnectionDataSource 
  * getExternalConnectionData


  * com.aspose.cells.ExternalConnection getExternalConnectionDataSource()
####  Returns 返回值 IExternalConnection


###  getFieldListSortAscending 
  * getFieldListSortAscending()boolean


  * boolean getFieldListSortAscending()
####  Returns 返回值 boolean


###  getGrandTotalName 
  * getGrandTotalName()string


  * java.lang.String getGrandTotalName()
####  Returns 返回值 string


###  getHorizontalBreaks 
  * getHorizontalBreaks()object[]


  * java.util.ArrayList getHorizontalBreaks()
####  Returns 返回值 object[]


###  getIndent 
  * getIndent()number


  * int getIndent()
####  Returns 返回值 number


###  getItemPrintTitles 
  * getItemPrintTitles()boolean


  * boolean getItemPrintTitles()
####  Returns 返回值 boolean


###  getManualUpdate 
  * getManualUpdate()boolean


  * boolean getManualUpdate()
####  Returns 返回值 boolean


###  getMergeLabels 
  * getMergeLabels()boolean


  * boolean getMergeLabels()
####  Returns 返回值 boolean


###  getMissingItemsLimit 
  * getMissingItemsLimit()number


  * int getMissingItemsLimit()
####  Returns 返回值 number


###  getName 
  * getName()string


  * java.lang.String getName()
####  Returns 返回值 string


###  getNullString 
  * getNullString()string


  * java.lang.String getNullString()
####  Returns 返回值 string


###  getPageFieldOrder 
  * getPageFieldOrder()number


  * int getPageFieldOrder()
####  Returns 返回值 number


###  getPageFieldWrapCount 
  * getPageFieldWrapCount()number


  * int getPageFieldWrapCount()
####  Returns 返回值 number


###  getPageFields 
  * getPageFields()IPivotFieldCollection


  * com.aspose.cells.PivotFieldCollection getPageFields()
####  Returns 返回值 IPivotFieldCollection


###  getPivotFilters 
  * getPivotFilters()IPivotFilterCollection


  * com.aspose.cells.PivotFilterCollection getPivotFilters()
####  Returns 返回值 IPivotFilterCollection


###  getPivotFormatConditions 
  * getPivotFormatConditions()IPivotFormatConditionCollection


  * com.aspose.cells.PivotFormatConditionCollection getPivotFormatConditions()
####  Returns 返回值 IPivotFormatConditionCollection


###  getPivotTableStyleName 
  * getPivotTableStyleName()string


  * java.lang.String getPivotTableStyleName()
####  Returns 返回值 string


###  getPivotTableStyleType 
  * getPivotTableStyleType()number


  * int getPivotTableStyleType()
####  Returns 返回值 number


###  getPreserveFormatting 
  * getPreserveFormatting()boolean


  * boolean getPreserveFormatting()
####  Returns 返回值 boolean


###  getPrintDrill 
  * getPrintDrill()boolean


  * boolean getPrintDrill()
####  Returns 返回值 boolean


###  getPrintTitles 
  * getPrintTitles()boolean


  * boolean getPrintTitles()
####  Returns 返回值 boolean


###  getRefreshDataFlag 
  * getRefreshDataFlag()boolean


  * boolean getRefreshDataFlag()
####  Returns 返回值 boolean


###  getRefreshDataOnOpeningFile 
  * getRefreshDataOnOpeningFile()boolean


  * boolean getRefreshDataOnOpeningFile()
####  Returns 返回值 boolean


###  getRefreshDate 
  * getRefresh


  * com.aspose.cells.DateTime getRefreshDate()
####  Returns 返回值 IDateTime


###  getRefreshedByWho 
  * getRefreshedByWho()string


  * java.lang.String getRefreshedByWho()
####  Returns 返回值 string


###  getRowFields 
  * getRowFields()IPivotFieldCollection


  * com.aspose.cells.PivotFieldCollection getRowFields()
####  Returns 返回值 IPivotFieldCollection


###  getRowGrand 
  * getRowGrand()boolean


  * boolean getRowGrand()
####  Returns 返回值 boolean


###  getRowHeaderCaption 
  * getRowHeaderCaption()string


  * java.lang.String getRowHeaderCaption()
####  Returns 返回值 string


###  getRowRange 
  * getRow


  * com.aspose.cells.CellArea getRowRange()
####  Returns 返回值 ICellArea


###  getSaveData 
  * getSaveData()boolean


  * boolean getSaveData()
####  Returns 返回值 boolean


###  getShowDataTips 
  * getShowDataTips()boolean


  * boolean getShowDataTips()
####  Returns 返回值 boolean


###  getShowDrill 
  * getShowDrill()boolean


  * boolean getShowDrill()
####  Returns 返回值 boolean


###  getShowEmpty
  * getShowEmptyCol()boolean


  * boolean getShowEmptyCol()
####  Returns 返回值 boolean


###  getShowEmpty
  * getShowEmptyRow()boolean


  * boolean getShowEmptyRow()
####  Returns 返回值 boolean


###  getShowMemberPropertyTips 
  * getShowMemberPropertyTips()boolean


  * boolean getShowMemberPropertyTips()
####  Returns 返回值 boolean


###  getShowPivotStyleColumnHeader 
  * getShowPivotStyleColumnHeader()boolean


  * boolean getShowPivotStyleColumnHeader()
####  Returns 返回值 boolean


###  getShowPivotStyleColumnStripes 
  * getShowPivotStyleColumnStripes()boolean


  * boolean getShowPivotStyleColumnStripes()
####  Returns 返回值 boolean


###  getShowPivotStyleLastColumn 
  * getShowPivotStyleLastColumn()boolean


  * boolean getShowPivotStyleLastColumn()
####  Returns 返回值 boolean


###  getShowPivotStyleRowHeader 
  * getShowPivotStyleRowHeader()boolean


  * boolean getShowPivotStyleRowHeader()
####  Returns 返回值 boolean


###  getShowPivotStyleRowStripes 
  * getShowPivotStyleRowStripes()boolean


  * boolean getShowPivotStyleRowStripes()
####  Returns 返回值 boolean


###  getShowRowHeaderCaption 
  * getShowRowHeaderCaption()boolean


  * boolean getShowRowHeaderCaption()
####  Returns 返回值 boolean


###  getShowValues
  * getShowValuesRow()boolean


  * boolean getShowValuesRow()
####  Returns 返回值 boolean


###  getSource 
  * getSource()string[]


  * java.lang.String[] getSource()
####  Returns 返回值 string[]


###  getSubtotalHiddenPageItems 
  * getSubtotalHiddenPageItems()boolean


  * boolean getSubtotalHiddenPageItems()
####  Returns 返回值 boolean


###  getTableRange1 
  * getTable


  * com.aspose.cells.CellArea getTableRange1()
####  Returns 返回值 ICellArea


###  getTableRange2 
  * getTable


  * com.aspose.cells.CellArea getTableRange2()
####  Returns 返回值 ICellArea


###  get 
  * getTag()string


  * java.lang.String getTag()
####  Returns 返回值 string


###  hasBlankRows 
  * hasBlankRows()boolean


  * boolean hasBlankRows()
####  Returns 返回值 boolean


###  isAutoFormat 
  * isAutoFormat()boolean


  * boolean isAutoFormat()
####  Returns 返回值 boolean


###  isExcel2003Compatible 
  * isExcel2003Compatible()boolean


  * boolean isExcel2003Compatible()
####  Returns 返回值 boolean


###  isGridDropZones 
  * isGridDropZones()boolean


  * boolean isGridDropZones()
####  Returns 返回值 boolean


###  isMultipleFieldFilters 
  * isMultipleFieldFilters()boolean


  * boolean isMultipleFieldFilters()
####  Returns 返回值 boolean


###  isSelected 
  * isSelected()boolean


  * boolean isSelected()
####  Returns 返回值 boolean


###  move 
  * move(rownumber, columnnumber)void
  * move(destCellNamestring)void


  * void move(int, int)
#### Parameters 参数
    * #####  row: number
    * #####  column: number
####  Returns 返回值 void
  * void move(java.lang.String)
#### Parameters 参数
    * #####  destCellName: string
####  Returns 返回值 void


###  refreshData 
  * refreshData()void


  * void refreshData()
####  Returns 返回值 void


###  removeField 
  * removeField(fieldTypenumber, pivotFieldIPivotField)void
  * removeField(fieldTypenumber, fieldNamestring)void
  * removeField(fieldTypenumber, baseFieldIndexnumber)void


  * void removeField(int, com.aspose.cells.PivotField)
#### Parameters 参数
    * #####  fieldType: number
    * #####  pivotField: IPivotField
####  Returns 返回值 void
  * void removeField(int, java.lang.String)
#### Parameters 参数
    * #####  fieldType: number
    * #####  fieldName: string
####  Returns 返回值 void
  * void removeField(int, int)
#### Parameters 参数
    * #####  fieldType: number
    * #####  baseFieldIndex: number
####  Returns 返回值 void


###  setAltTextDescription 
  * setAltTextDescription(valuestring)void


  * void setAltTextDescription(java.lang.String)
#### Parameters 参数
    * #####  value: string
####  Returns 返回值 void


###  setAltTextTitle 
  * setAltTextTitle(valuestring)void


  * void setAltTextTitle(java.lang.String)
#### Parameters 参数
    * #####  value: string
####  Returns 返回值 void


###  setAutoFormat 
  * setAutoFormat(valueboolean)void


  * void setAutoFormat(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setAutoFormatType 
  * setAutoFormatType(valuenumber)void


  * void setAutoFormatType(int)
#### Parameters 参数
    * #####  value: number
####  Returns 返回值 void


###  setAutoGroupField 
  * setAutoGroupField(baseFieldIndexnumber)void
  * setAutoGroupField(pivotFieldIPivotField)void


  * void setAutoGroupField(int)
#### Parameters 参数
    * #####  baseFieldIndex: number
####  Returns 返回值 void
  * void setAutoGroupField(com.aspose.cells.PivotField)
#### Parameters 参数
    * #####  pivotField: IPivotField
####  Returns 返回值 void


###  setColumnGrand 
  * setColumnGrand(valueboolean)void


  * void setColumnGrand(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setColumnHeaderCaption 
  * setColumnHeaderCaption(valuestring)void


  * void setColumnHeaderCaption(java.lang.String)
#### Parameters 参数
    * #####  value: string
####  Returns 返回值 void


###  setCustomListSort 
  * setCustomListSort(valueboolean)void


  * void setCustomListSort(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setDataSource 
  * setDataSource(valuestring[])void


  * void setDataSource(java.lang.String[])
#### Parameters 参数
    * #####  value: string[]
####  Returns 返回值 void


###  setDisplayErrorString 
  * setDisplayErrorString(valueboolean)void


  * void setDisplayErrorString(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setDisplayImmediateItems 
  * setDisplayImmediateItems(valueboolean)void


  * void setDisplayImmediateItems(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setDisplayNullString 
  * setDisplayNullString(valueboolean)void


  * void setDisplayNullString(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setEnableDataValueEditing 
  * setEnableDataValueEditing(valueboolean)void


  * void setEnableDataValueEditing(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setEnableDrilldown 
  * setEnableDrilldown(valueboolean)void


  * void setEnableDrilldown(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setEnableFieldDialog 
  * setEnableFieldDialog(valueboolean)void


  * void setEnableFieldDialog(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setEnableFieldList 
  * setEnableFieldList(valueboolean)void


  * void setEnableFieldList(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setEnableWizard 
  * setEnableWizard(valueboolean)void


  * void setEnableWizard(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setErrorString 
  * setErrorString(valuestring)void


  * void setErrorString(java.lang.String)
#### Parameters 参数
    * #####  value: string
####  Returns 返回值 void


###  setExcel2003Compatible 
  * setExcel2003Compatible(valueboolean)void


  * void setExcel2003Compatible(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setFieldListSortAscending 
  * setFieldListSortAscending(valueboolean)void


  * void setFieldListSortAscending(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setGrandTotalName 
  * setGrandTotalName(valuestring)void


  * void setGrandTotalName(java.lang.String)
#### Parameters 参数
    * #####  value: string
####  Returns 返回值 void


###  setGridDropZones 
  * setGridDropZones(valueboolean)void


  * void setGridDropZones(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setHasBlankRows 
  * setHasBlankRows(valueboolean)void


  * void setHasBlankRows(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setIndent 
  * setIndent(valuenumber)void


  * void setIndent(int)
#### Parameters 参数
    * #####  value: number
####  Returns 返回值 void


###  setItemPrintTitles 
  * setItemPrintTitles(valueboolean)void


  * void setItemPrintTitles(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setManualGroupField 
  * setManualGroupField(pivotFieldIPivotField, startValIDateTime, endValIDateTime, groupByListobject[], intervalNumnumber)void
  * setManualGroupField(baseFieldIndexnumber, startValIDateTime, endValIDateTime, groupByListobject[], intervalNumnumber)void
  * setManualGroupField(pivotFieldIPivotField, startValnumber, endValnumber, groupByListobject[], intervalNumnumber)void
  * setManualGroupField(baseFieldIndexnumber, startValnumber, endValnumber, groupByListobject[], intervalNumnumber)void


  * void setManualGroupField(com.aspose.cells.PivotField, com.aspose.cells.DateTime, com.aspose.cells.DateTime, java.util.ArrayList, int)
#### Parameters 参数
    * #####  pivotField: IPivotField
    * #####  startVal: IDateTime
    * #####  endVal: IDateTime
    * #####  groupByList: object[]
    * #####  intervalNum: number
####  Returns 返回值 void
  * void setManualGroupField(int, com.aspose.cells.DateTime, com.aspose.cells.DateTime, java.util.ArrayList, int)
#### Parameters 参数
    * #####  baseFieldIndex: number
    * #####  startVal: IDateTime
    * #####  endVal: IDateTime
    * #####  groupByList: object[]
    * #####  intervalNum: number
####  Returns 返回值 void
  * void setManualGroupField(com.aspose.cells.PivotField, double, double, java.util.ArrayList, double)
#### Parameters 参数
    * #####  pivotField: IPivotField
    * #####  startVal: number
    * #####  endVal: number
    * #####  groupByList: object[]
    * #####  intervalNum: number
####  Returns 返回值 void
  * void setManualGroupField(int, double, double, java.util.ArrayList, double)
#### Parameters 参数
    * #####  baseFieldIndex: number
    * #####  startVal: number
    * #####  endVal: number
    * #####  groupByList: object[]
    * #####  intervalNum: number
####  Returns 返回值 void


###  setManualUpdate 
  * setManualUpdate(valueboolean)void


  * void setManualUpdate(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setMergeLabels 
  * setMergeLabels(valueboolean)void


  * void setMergeLabels(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setMissingItemsLimit 
  * setMissingItemsLimit(valuenumber)void


  * void setMissingItemsLimit(int)
#### Parameters 参数
    * #####  value: number
####  Returns 返回值 void


###  setMultipleFieldFilters 
  * setMultipleFieldFilters(valueboolean)void


  * void setMultipleFieldFilters(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setName 
  * setName(valuestring)void


  * void setName(java.lang.String)
#### Parameters 参数
    * #####  value: string
####  Returns 返回值 void


###  setNullString 
  * setNullString(valuestring)void


  * void setNullString(java.lang.String)
#### Parameters 参数
    * #####  value: string
####  Returns 返回值 void


###  setPageFieldOrder 
  * setPageFieldOrder(valuenumber)void


  * void setPageFieldOrder(int)
#### Parameters 参数
    * #####  value: number
####  Returns 返回值 void


###  setPageFieldWrapCount 
  * setPageFieldWrapCount(valuenumber)void


  * void setPageFieldWrapCount(int)
#### Parameters 参数
    * #####  value: number
####  Returns 返回值 void


###  setPivotTableStyleName 
  * setPivotTableStyleName(valuestring)void


  * void setPivotTableStyleName(java.lang.String)
#### Parameters 参数
    * #####  value: string
####  Returns 返回值 void


###  setPivotTableStyleType 
  * setPivotTableStyleType(valuenumber)void


  * void setPivotTableStyleType(int)
#### Parameters 参数
    * #####  value: number
####  Returns 返回值 void


###  setPreserveFormatting 
  * setPreserveFormatting(valueboolean)void


  * void setPreserveFormatting(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setPrintDrill 
  * setPrintDrill(valueboolean)void


  * void setPrintDrill(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setPrintTitles 
  * setPrintTitles(valueboolean)void


  * void setPrintTitles(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setRefreshDataFlag 
  * setRefreshDataFlag(valueboolean)void


  * void setRefreshDataFlag(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setRefreshDataOnOpeningFile 
  * setRefreshDataOnOpeningFile(valueboolean)void


  * void setRefreshDataOnOpeningFile(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setRowGrand 
  * setRowGrand(valueboolean)void


  * void setRowGrand(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setRowHeaderCaption 
  * setRowHeaderCaption(valuestring)void


  * void setRowHeaderCaption(java.lang.String)
#### Parameters 参数
    * #####  value: string
####  Returns 返回值 void


###  setSaveData 
  * setSaveData(valueboolean)void


  * void setSaveData(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setSelected 
  * setSelected(valueboolean)void


  * void setSelected(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setShowDataTips 
  * setShowDataTips(valueboolean)void


  * void setShowDataTips(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setShowDrill 
  * setShowDrill(valueboolean)void


  * void setShowDrill(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setShowEmpty
  * setShowEmptyCol(valueboolean)void


  * void setShowEmptyCol(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setShowEmpty
  * setShowEmptyRow(valueboolean)void


  * void setShowEmptyRow(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setShowMemberPropertyTips 
  * setShowMemberPropertyTips(valueboolean)void


  * void setShowMemberPropertyTips(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setShowPivotStyleColumnHeader 
  * setShowPivotStyleColumnHeader(valueboolean)void


  * void setShowPivotStyleColumnHeader(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setShowPivotStyleColumnStripes 
  * setShowPivotStyleColumnStripes(valueboolean)void


  * void setShowPivotStyleColumnStripes(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setShowPivotStyleLastColumn 
  * setShowPivotStyleLastColumn(valueboolean)void


  * void setShowPivotStyleLastColumn(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setShowPivotStyleRowHeader 
  * setShowPivotStyleRowHeader(valueboolean)void


  * void setShowPivotStyleRowHeader(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setShowPivotStyleRowStripes 
  * setShowPivotStyleRowStripes(valueboolean)void


  * void setShowPivotStyleRowStripes(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setShowRowHeaderCaption 
  * setShowRowHeaderCaption(valueboolean)void


  * void setShowRowHeaderCaption(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setShowValues
  * setShowValuesRow(valueboolean)void


  * void setShowValuesRow(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  setSubtotalHiddenPageItems 
  * setSubtotalHiddenPageItems(valueboolean)void


  * void setSubtotalHiddenPageItems(boolean)
#### Parameters 参数
    * #####  value: boolean
####  Returns 返回值 void


###  set 
  * setTag(valuestring)void


  * void setTag(java.lang.String)
#### Parameters 参数
    * #####  value: string
####  Returns 返回值 void


###  setUngroup 
  * setUngroup(baseFieldIndexnumber)void
  * setUngroup(pivotFieldIPivotField)void


  * void setUngroup(int)
#### Parameters 参数
    * #####  baseFieldIndex: number
####  Returns 返回值 void
  * void setUngroup(com.aspose.cells.PivotField)
#### Parameters 参数
    * #####  pivotField: IPivotField
####  Returns 返回值 void


###  showInCompactForm 
  * showInCompactForm()void


  * void showInCompactForm()
####  Returns 返回值 void


###  showInOutlineForm 
  * showInOutlineForm()void


  * void showInOutlineForm()
####  Returns 返回值 void


###  showInTabularForm 
  * showInTabularForm()void


  * void showInTabularForm()
####  Returns 返回值 void


###  showReportFilterPage 
  * showReportFilterPage(pageFieldIPivotField)void


  * void showReportFilterPage(com.aspose.cells.PivotField)
#### Parameters 参数
    * #####  pageField: IPivotField
####  Returns 返回值 void


###  showReportFilterPageByIndex 
  * showReportFilterPageByIndex(posIndexnumber)void


  * void showReportFilterPageByIndex(int)
#### Parameters 参数
    * #####  posIndex: number
####  Returns 返回值 void


###  showReportFilterPageByName 
  * showReportFilterPageByName(fieldNamestring)void


  * void showReportFilterPageByName(java.lang.String)
#### Parameters 参数
    * #####  fieldName: string
####  Returns 返回值 void



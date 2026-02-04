com.aspose.cells.ShapeCollection
### Hierarchy 层级
  * ICollectionBase
    * IShapeCollection


## Index 目录
###  Methods 方法 
  * addActiveXControl
  * addAutoShape
  * addAutoShapeInChart
  * addFreeFloatingShape
  * addLabelInChart
  * addLinkedPicture
  * addOleObject
  * addOleObjectWithLinkedImage
  * addPictureInChart
  * addShapeInChart
  * addTextBoxInChart
  * addTextEffect
  * addTextEffectInChart
  * copyCommentsInRange
  * copyInRange
  * deleteInRange
  * deleteShape
  * updateSelectedValue


##  Methods 方法 
###  add 
  * add(oany)number


  * int add(java.lang.Object)
#### Parameters 参数
####  Returns 返回值 number


###  addActiveXControl 
  * addActiveXControl(typenumber, topRownumber, topnumber, leftColumnnumber, leftnumber, widthnumber, heightnumber)IShape


  * com.aspose.cells.Shape addActiveXControl(int, int, int, int, int, int, int)
#### Parameters 参数
    * #####  type: number
    * #####  topRow: number
    * #####  top: number
    * #####  leftColumn: number
    * #####  left: number
    * #####  width: number
    * #####  height: number
####  Returns 返回值 IShape


###  addAutoShape 
  * addAutoShape(typenumber, upperLeftRownumber, topnumber, upperLeftColumnnumber, leftnumber, heightnumber, widthnumber)IShape


  * com.aspose.cells.Shape addAutoShape(int, int, int, int, int, int, int)
#### Parameters 参数
    * #####  type: number
    * #####  upperLeftRow: number
    * #####  top: number
    * #####  upperLeftColumn: number
    * #####  left: number
    * #####  height: number
    * #####  width: number
####  Returns 返回值 IShape


###  addAutoShapeInChart 
  * addAutoShapeInChart(typenumber, topnumber, leftnumber, heightnumber, widthnumber)IShape


  * com.aspose.cells.Shape addAutoShapeInChart(int, int, int, int, int)
#### Parameters 参数
    * #####  type: number
    * #####  top: number
    * #####  left: number
    * #####  height: number
    * #####  width: number
####  Returns 返回值 IShape


###  addCopy 
  * addCopy(sourceShapeIShape, upperLeftRownumber, topnumber, upperLeftColumnnumber, leftnumber)IShape


  * com.aspose.cells.Shape addCopy(com.aspose.cells.Shape, int, int, int, int)
#### Parameters 参数
    * #####  sourceShape: IShape
    * #####  upperLeftRow: number
    * #####  top: number
    * #####  upperLeftColumn: number
    * #####  left: number
####  Returns 返回值 IShape


###  addFreeFloatingShape 
  * addFreeFloatingShape(typenumber, topnumber, leftnumber, heightnumber, widthnumber, imageDatanumber[], isOriginalSizeboolean)IShape


  * com.aspose.cells.Shape addFreeFloatingShape(int, int, int, int, int, byte[], boolean)
#### Parameters 参数
    * #####  type: number
    * #####  top: number
    * #####  left: number
    * #####  height: number
    * #####  width: number
    * #####  imageData: number[]
    * #####  isOriginalSize: boolean
####  Returns 返回值 IShape


###  addLabelInChart 
  * addLabelInChart(topnumber, leftnumber, heightnumber, widthnumber)ILabel


  * com.aspose.cells.Label addLabelInChart(int, int, int, int)
#### Parameters 参数
    * #####  top: number
    * #####  left: number
    * #####  height: number
    * #####  width: number
####  Returns 返回值 ILabel


###  addLinkedPicture 
  * addLinkedPicture(upperLeftRownumber, upperLeftColumnnumber, heightnumber, widthnumber, sourceFullNamestring)IPicture


  * com.aspose.cells.Picture addLinkedPicture(int, int, int, int, java.lang.String)
#### Parameters 参数
    * #####  upperLeftRow: number
    * #####  upperLeftColumn: number
    * #####  height: number
    * #####  width: number
    * #####  sourceFullName: string
####  Returns 返回值 IPicture


###  addOleObject 
  * addOleObject(upperLeftRownumber, topnumber, upperLeftColumnnumber, leftnumber, heightnumber, widthnumber, imageDatanumber[])IOleObject


  * com.aspose.cells.OleObject addOleObject(int, int, int, int, int, int, byte[])
#### Parameters 参数
    * #####  upperLeftRow: number
    * #####  top: number
    * #####  upperLeftColumn: number
    * #####  left: number
    * #####  height: number
    * #####  width: number
    * #####  imageData: number[]
####  Returns 返回值 IOleObject


###  addOleObjectWithLinkedImage 
  * addOleObjectWithLinkedImage(upperLeftRownumber, upperLeftColumnnumber, heightnumber, widthnumber, sourceFullNamestring)IOleObject


  * com.aspose.cells.OleObject addOleObjectWithLinkedImage(int, int, int, int, java.lang.String)
#### Parameters 参数
    * #####  upperLeftRow: number
    * #####  upperLeftColumn: number
    * #####  height: number
    * #####  width: number
    * #####  sourceFullName: string
####  Returns 返回值 IOleObject


###  addPicture 
  * addPicture(upperLeftRownumber, upperLeftColumnnumber, streamany, widthScalenumber, heightScalenumber)IPicture
  * addPicture(upperLeftRownumber, upperLeftColumnnumber, lowerRightRownumber, lowerRightColumnnumber, streamany)IPicture


  * com.aspose.cells.Picture addPicture(int, int, java.io.InputStream, int, int)
#### Parameters 参数
    * #####  upperLeftRow: number
    * #####  upperLeftColumn: number
    * #####  stream: any
    * #####  widthScale: number
    * #####  heightScale: number
####  Returns 返回值 IPicture
  * com.aspose.cells.Picture addPicture(int, int, int, int, java.io.InputStream)
#### Parameters 参数
    * #####  upperLeftRow: number
    * #####  upperLeftColumn: number
    * #####  lowerRightRow: number
    * #####  lowerRightColumn: number
    * #####  stream: any
####  Returns 返回值 IPicture


###  addPictureInChart 
  * addPictureInChart(topnumber, leftnumber, streamany, widthScalenumber, heightScalenumber)IPicture


  * com.aspose.cells.Picture addPictureInChart(int, int, java.io.InputStream, int, int)
#### Parameters 参数
    * #####  top: number
    * #####  left: number
    * #####  stream: any
    * #####  widthScale: number
    * #####  heightScale: number
####  Returns 返回值 IPicture


###  addShape 
  * addShape(typenumber, upperLeftRownumber, topnumber, upperLeftColumnnumber, leftnumber, heightnumber, widthnumber)IShape


  * com.aspose.cells.Shape addShape(int, int, int, int, int, int, int)
#### Parameters 参数
    * #####  type: number
    * #####  upperLeftRow: number
    * #####  top: number
    * #####  upperLeftColumn: number
    * #####  left: number
    * #####  height: number
    * #####  width: number
####  Returns 返回值 IShape


###  addShapeInChart 
  * addShapeInChart(typenumber, placementnumber, leftnumber, topnumber, rightnumber, bottomnumber, imageDatanumber[])IShape
  * addShapeInChart(typenumber, placementnumber, leftnumber, topnumber, rightnumber, bottomnumber)IShape


  * com.aspose.cells.Shape addShapeInChart(int, int, int, int, int, int, byte[])
#### Parameters 参数
    * #####  type: number
    * #####  placement: number
    * #####  left: number
    * #####  top: number
    * #####  right: number
    * #####  bottom: number
    * #####  imageData: number[]
####  Returns 返回值 IShape
  * com.aspose.cells.Shape addShapeInChart(int, int, int, int, int, int)
#### Parameters 参数
    * #####  type: number
    * #####  placement: number
    * #####  left: number
    * #####  top: number
    * #####  right: number
    * #####  bottom: number
####  Returns 返回值 IShape


###  add 
  * addSvg(upperLeftRownumber, topnumber, upperLeftColumnnumber, leftnumber, heightnumber, widthnumber, svgDatanumber[], compatibleImageDatanumber[])IPicture


  * com.aspose.cells.Picture addSvg(int, int, int, int, int, int, byte[], byte[])
#### Parameters 参数
    * #####  upperLeftRow: number
    * #####  top: number
    * #####  upperLeftColumn: number
    * #####  left: number
    * #####  height: number
    * #####  width: number
    * #####  svgData: number[]
    * #####  compatibleImageData: number[]
####  Returns 返回值 IPicture


###  addTextBoxInChart 
  * addTextBoxInChart(topnumber, leftnumber, heightnumber, widthnumber)ITextBox


  * com.aspose.cells.TextBox addTextBoxInChart(int, int, int, int)
#### Parameters 参数
    * #####  top: number
    * #####  left: number
    * #####  height: number
    * #####  width: number
####  Returns 返回值 ITextBox


###  addTextEffect 
  * addTextEffect(effectnumber, textstring, fontNamestring, sizenumber, fontBoldboolean, fontItalicboolean, upperLeftRownumber, topnumber, upperLeftColumnnumber, leftnumber, heightnumber, widthnumber)IShape


  * com.aspose.cells.Shape addTextEffect(int, java.lang.String, java.lang.String, int, boolean, boolean, int, int, int, int, int, int)
#### Parameters 参数
    * #####  effect: number
    * #####  text: string
    * #####  fontName: string
    * #####  size: number
    * #####  fontBold: boolean
    * #####  fontItalic: boolean
    * #####  upperLeftRow: number
    * #####  top: number
    * #####  upperLeftColumn: number
    * #####  left: number
    * #####  height: number
    * #####  width: number
####  Returns 返回值 IShape


###  addTextEffectInChart 
  * addTextEffectInChart(effectnumber, textstring, fontNamestring, sizenumber, fontBoldboolean, fontItalicboolean, topnumber, leftnumber, heightnumber, widthnumber)IShape


  * com.aspose.cells.Shape addTextEffectInChart(int, java.lang.String, java.lang.String, int, boolean, boolean, int, int, int, int)
#### Parameters 参数
    * #####  effect: number
    * #####  text: string
    * #####  fontName: string
    * #####  size: number
    * #####  fontBold: boolean
    * #####  fontItalic: boolean
    * #####  top: number
    * #####  left: number
    * #####  height: number
    * #####  width: number
####  Returns 返回值 IShape


###  addWord
  * addWordArt(stylenumber, textstring, upperLeftRownumber, topnumber, upperLeftColumnnumber, leftnumber, heightnumber, widthnumber)IShape


  * com.aspose.cells.Shape addWordArt(int, java.lang.String, int, int, int, int, int, int)
#### Parameters 参数
    * #####  style: number
    * #####  text: string
    * #####  upperLeftRow: number
    * #####  top: number
    * #####  upperLeftColumn: number
    * #####  left: number
    * #####  height: number
    * #####  width: number
####  Returns 返回值 IShape


###  clear 
  * clear()void


  * void clear()
####  Returns 返回值 void


###  contains 
  * contains(oany)boolean


  * boolean contains(java.lang.Object)
#### Parameters 参数
####  Returns 返回值 boolean


###  copyCommentsInRange 
  * copyCommentsInRange(shapesIShapeCollection, caICellArea, destRownumber, destColumnnumber)void


  * void copyCommentsInRange(com.aspose.cells.ShapeCollection, com.aspose.cells.CellArea, int, int)
#### Parameters 参数
    * #####  shapes: IShapeCollection
    *     * #####  destRow: number
    * #####  destColumn: number
####  Returns 返回值 void


###  copyInRange 
  * copyInRange(sourceShapesIShapeCollection, caICellArea, destRownumber, destColumnnumber, isContainedboolean)void


  * void copyInRange(com.aspose.cells.ShapeCollection, com.aspose.cells.CellArea, int, int, boolean)
#### Parameters 参数
    * #####  sourceShapes: IShapeCollection
    *     * #####  destRow: number
    * #####  destColumn: number
    * #####  isContained: boolean
####  Returns 返回值 void


###  deleteInRange 
  * deleteInRange(caICellArea)void


  * void deleteInRange(com.aspose.cells.CellArea)
#### Parameters 参数
    * ####  Returns 返回值 void


###  deleteShape 
  * deleteShape(shapeIShape)void


  * void deleteShape(com.aspose.cells.Shape)
#### Parameters 参数
    * #####  shape: IShape
####  Returns 返回值 void


###  get 
  * get(indexnumber)any
  * get(namestring)IShape


  * java.lang.Object get(int)
#### Parameters 参数
    * #####  index: number
####  Returns 返回值 any
  * com.aspose.cells.Shape get(java.lang.String)
#### Parameters 参数
    * #####  name: string
####  Returns 返回值 IShape


###  getCount 
  * getCount()number


  * int getCount()
####  Returns 返回值 number


###  group 
  * group(groupItemsIShape[])IGroupShape


  * com.aspose.cells.GroupShape group(com.aspose.cells.Shape[])
#### Parameters 参数
    * #####  groupItems: IShape[]
####  Returns 返回值 IGroupShape


###  index 
  * indexOf(oany)number


  * int indexOf(java.lang.Object)
#### Parameters 参数
####  Returns 返回值 number


###  iterator 
  * iterator()any


  * java.util.Iterator iterator()
####  Returns 返回值 any


###  remove 
  * remove(shapeIShape)void


  * void remove(com.aspose.cells.Shape)
#### Parameters 参数
    * #####  shape: IShape
####  Returns 返回值 void


###  remove 
  * removeAt(indexnumber)void


  * void removeAt(int)
#### Parameters 参数
    * #####  index: number
####  Returns 返回值 void


###  ungroup 
  * ungroup(groupIGroupShape)void


  * void ungroup(com.aspose.cells.GroupShape)
#### Parameters 参数
    * #####  group: IGroupShape
####  Returns 返回值 void


###  updateSelectedValue 
  * updateSelectedValue()void


  * void updateSelectedValue()
####  Returns 返回值 void



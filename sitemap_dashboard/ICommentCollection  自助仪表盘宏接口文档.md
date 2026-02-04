com.aspose.cells.CommentCollection
### Hierarchy 层级
  * ICollectionBase
    * ICommentCollection


## Index 目录
###  Methods 方法 
  * addThreadedComment
  * getThreadedComments


##  Methods 方法 
###  add 
  * add(oany)number
  * add(cellNamestring)number
  * add(rownumber, columnnumber)number


  * int add(java.lang.Object)
#### Parameters 参数
####  Returns 返回值 number
  * int add(java.lang.String)
#### Parameters 参数
    * #####  cellName: string
####  Returns 返回值 number
  * int add(int, int)
#### Parameters 参数
    * #####  row: number
    * #####  column: number
####  Returns 返回值 number


###  addThreadedComment 
  * addThreadedComment(cellNamestring, textstring, authorIThreadedCommentAuthor)number
  * addThreadedComment(rownumber, columnnumber, textstring, authorIThreadedCommentAuthor)number


  * int addThreadedComment(java.lang.String, java.lang.String, com.aspose.cells.ThreadedCommentAuthor)
#### Parameters 参数
    * #####  cellName: string
    * #####  text: string
    * #####  author: IThreadedCommentAuthor
####  Returns 返回值 number
  * int addThreadedComment(int, int, java.lang.String, com.aspose.cells.ThreadedCommentAuthor)
#### Parameters 参数
    * #####  row: number
    * #####  column: number
    * #####  text: string
    * #####  author: IThreadedCommentAuthor
####  Returns 返回值 number


###  clear 
  * clear()void


  * void clear()
####  Returns 返回值 void


###  contains 
  * contains(oany)boolean


  * boolean contains(java.lang.Object)
#### Parameters 参数
####  Returns 返回值 boolean


###  get 
  * get(cellNamestring)IComment
  * get(indexnumber)any
  * get(rownumber, columnnumber)IComment


  * com.aspose.cells.Comment get(java.lang.String)
#### Parameters 参数
    * #####  cellName: string
####  Returns 返回值 IComment
  * java.lang.Object get(int)
#### Parameters 参数
    * #####  index: number
####  Returns 返回值 any
  * com.aspose.cells.Comment get(int, int)
#### Parameters 参数
    * #####  row: number
    * #####  column: number
####  Returns 返回值 IComment


###  getCount 
  * getCount()number


  * int getCount()
####  Returns 返回值 number


###  getThreadedComments 
  * getThreadedComments(rownumber, columnnumber)IThreadedCommentCollection
  * getThreadedComments(cellNamestring)IThreadedCommentCollection


  * com.aspose.cells.ThreadedCommentCollection getThreadedComments(int, int)
#### Parameters 参数
    * #####  row: number
    * #####  column: number
####  Returns 返回值 IThreadedCommentCollection
  * com.aspose.cells.ThreadedCommentCollection getThreadedComments(java.lang.String)
#### Parameters 参数
    * #####  cellName: string
####  Returns 返回值 IThreadedCommentCollection


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
  * removeAt(indexnumber)void
  * removeAt(cellNamestring)void
  * removeAt(rownumber, columnnumber)void


  * void removeAt(int)
#### Parameters 参数
    * #####  index: number
####  Returns 返回值 void
  * void removeAt(java.lang.String)
#### Parameters 参数
    * #####  cellName: string
####  Returns 返回值 void
  * void removeAt(int, int)
#### Parameters 参数
    * #####  row: number
    * #####  column: number
####  Returns 返回值 void



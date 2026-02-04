#### 通过
# MDX 数据定义 - CREATE ACTION
创建可与多维数据集、维度、层次结构或从属对象关联的作。
```
  
CREATE ACTION CURRENTCUBE | Cube_Name  
   .Action_Name <action body>  
<action body> ::=   
FOR   
        CUBE   
    | Hierarchy_Name [MEMBERS]   
    | Level_Name [MEMBERS]   
    | CELLS   
    | SET }   
      AS 'MDX_Expression'   
        [, TYPE = '  
              { URL   
            | HTML   
            | STATEMENT   
               | DATASET   
            | ROWSET   
            | COMMANDLINE   
               | PROPRIETARY }   
         ']  
   [ , INVOCATION = 'INTERACTIVE | ON_OPEN | BATCH ' ]  
   [ , APPLICATION = String_Expression ]  
   [ , DESCRIPTION = String_Expression ]  
   [ , CAPTION = 'MDX_Expression' ]  

```

_Cube_Name_ 提供多维数据集名称的有效字符串。
_Action_名称_ 一个提供所创建作的名称的有效字符串。
_Hierarchy_名称_ 提供层次结构名称的有效字符串。
_Level_名称_ 提供级别名称的有效字符串。
_Member_名称_ 提供成员名称或成员密钥的有效字符串。
_MDX_Expression_ 有效的 MDX 表达式。
_String_Expression_ 有效的字符串表达式。
客户端应用程序可以创建和运行不安全的作;客户端应用程序也可以使用不安全的函数。 若要避免这些情况，请使用 **“安全选项”** 属性。 有关详细信息，请参阅“安全选项”属性。
此语句是为向后兼容性而包含的。 不支持 Analysis Services 的新作，例如钻取或报表作。
下表描述了 Analysis Services 中可用的不同类型的作。
操作类型 | DESCRIPTION  
---|---  
返回的作字符串是应使用 Internet 浏览器打开的 URL。 注意：如果此作未启动 `https://` ，或者 `https://`，除非 **SafetyOptions** 设置为 **DBPROPVAL_MSMD_SAFETY_OPTIONS_ALLOW_ALL** ，否则该作将不可用。  
返回的作字符串是一个 HTML 脚本。 字符串应保存到文件中，并且应使用 Internet 浏览器呈现该文件。 在这种情况下，整个脚本可以作为生成的 HTML 的一部分运行。  
返回的作字符串是一个语句，需要通过将命令对象的 **ICommand：：SetText** 方法设置为字符串并调用 **ICommand：：Execute** 方法来执行该语句。 如果命令未成功，则返回错误。  
返回的作字符串是一个 MDX 语句，需要通过将命令对象的 **ICommand：：SetText** 方法设置为字符串并调用 **ICommand：：Execute** 方法来运行该语句。 请求的接口 ID （IID） 应为 **IDataset** 。 如果已创建数据集，该命令将成功。 客户端应用程序应允许用户浏览返回的数据集。  
与 **DATASET** 类似，但客户端应用程序应请求 **IRowset** 的 IID，而不是请求 **IDataset** 的 IID。 如果已创建行集，该命令将成功。 客户端应用程序应允许用户浏览返回的行集。  
**COMMANDLINE** | 客户端应用程序应执行作字符串。 字符串是命令行。  
除非应用程序具有对特定作的自定义非常规知识，否则客户端应用程序不应显示或执行该作。 除非客户端应用程序通过对 **APPLICATION_NAME** 设置适当的限制来显式请求这些作，否则不会将专有作返回到客户端应用程序。  
下表描述了 Analysis Services 中可用的不同类型的调用。 调用类型仅由客户端应用程序用来帮助确定何时调用作。 调用类型实际上不会确定作的调用行为。
调用类型 | DESCRIPTION  
---|---  
该作应由客户端应用程序通过用户交互调用。  
**ON_OPEN** | 打开目标对象时，客户端应用程序应调用该作。 此调用类型当前未实现。  
当目标对象参与批处理作时，客户端应用程序应调用该作，由客户端应用程序确定。 此调用类型当前未实现。  
每个作都为特定多维数据集定义，并在该多维数据集中具有唯一的名称。 作可以包含下表中列出的范围之一。
多维数据集范围 对于独立于特定维度、成员或单元格的作;例如：“AS/400 生产系统的启动终端仿真”。
维度范围 该作适用于特定维度。 这些作不依赖于特定级别的选择或成员。
级别范围 该作适用于特定的维度级别。 这些作不依赖于该维度中成员的特定选择。
成员范围 该作适用于特定级别成员。
单元格范围 该作仅适用于特定单元格。
设置作用域 该作仅适用于集。 名称 **ActionParameterSet** 保留供应用程序在作表达式内使用。
1月27日 15时 - 1月27日 15时 



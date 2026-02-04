
## 示例效果
在电子表格中对序号进行倒序显示，如图：
## 实现步骤
1、新建电子表格  
---  
2、设置序号 |  在C3单元格中输入公式“=COUNTA(SSR_GetSubCells(A3))-SSR_GetIndex(A3)”，如图： 公式说明如下： 1）COUNTA（）：计算区域中非空单元格的个数。 2）SSR_GetSubCells：详情请参考 SSR_GetSubCells。 3）SSR_GetIndex：详情请参考 SSR_GetIndex。 公式“=COUNTA(SSR_GetSubCells(A3))-SSR_GetIndex(A3)”：表示先计算A3单元格的数据总数，然后将总数减去当前数据在表格区域中的行数。 如果“序号”列放在“发货区域”列的左侧，则需指定序号公式所在的单元格的左父格为“发货区域”数据列字段所在的单元格。  
## 示例资源  

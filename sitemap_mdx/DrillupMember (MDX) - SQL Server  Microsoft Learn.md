#### 通过
# DrillupMember (MDX)
返回指定集中不是第二个指定集中成员的后代的成员。
```
  
DrillupMember(Set_Expression1, Set_Expression2)   

```

_Set_Expression1_ 返回集的有效多维表达式 (MDX)。
_Set_Expression2_ 返回集的有效多维表达式 (MDX)。
**DrillupMember** 函数基于第一组中指定的成员返回一组成员，这些成员是第二组成员的后代。 第一个集可以具有任何维数，但第二个集必须包含一个一维集。 第一个集中的原始成员顺序会被保留。 此函数在构造集时仅包括位于第一个集中并且是第二个集中成员的直接后代的那些成员。 如果第一个集中某成员的直接祖先不在第二个集中，则第一个集中的该成员包括在此函数返回的集中。 第一个集中位于第二个集中某个祖先成员之前的后代，也会包括在内。
第一个集可以包含元组，但不能包含成员。 元组的深化是 OLE DB 的扩展，它返回元组集而非成员集。
只有后面紧跟子成员或后代的成员才会被浅化。 成员集中成员的顺序对于 Drilldown* 和 Drillup* 系列的函数非常重要。 请考虑使用 **Hierarchize** 函数对第一组的成员进行适当的排序。
除了第二个集以外，以下三个示例都是相似的。 在第一个示例时，第二个集为 United States。 因此，从结果集中排除 Colorado。 它是 United States 的后代。
```
SELECT DrillUpMember (   
  { [Geography].[Geography].[Country].[Canada]   
   ,[Geography].[Geography].[Country].[United States]   
   ,[Geography].[Geography].[State-Province].[Colorado]   
   ,[Geography].[Geography].[State-Province].[Alberta]   
   ,[Geography].[Geography].[State-Province].[Brunswick]    
 }   
 , {[Geography].[Geography].[Country].[United States]}   
 ) ON 0   
FROM [Adventure Works]  

```

示例二向我们显示了成员顺序的重要性。 由于 **DrillupMember** 仅钻取第一组紧随后代的那些成员，因此它不会向上钻取加拿大成员。 Canada 与其后代由 United States 和 Colorado 分隔开来。 如果你对成员重新排序，使 Canada 直接位于 Alberta 上方，则 Alberta 和 Brunswick 都将从行集中排除。
```
SELECT DrillUpMember (   
 {  [Geography].[Geography].[Country].[Canada]   
   ,[Geography].[Geography].[Country].[United States]   
   ,[Geography].[Geography].[State-Province].[Colorado]   
   ,[Geography].[Geography].[State-Province].[Alberta]   
   ,[Geography].[Geography].[State-Province].[Brunswick]    
 }   
 , {[Geography].[Geography].[Country].[Canada]}   
 )   
ON 0   
FROM [Adventure Works]  

```

示例 3 演示了使用 **层次结构** 如何减轻成员顺序的影响，以及如何向上钻取加拿大成员。
```
SELECT DrillUpMember (   
 Hierarchize   
  (   
   { [Geography].[Geography].[Country].[Canada]   
    ,[Geography].[Geography].[Country].[United States]   
    ,[Geography].[Geography].[State-Province].[Colorado]   
    ,[Geography].[Geography].[State-Province].[Alberta]   
    ,[Geography].[Geography].[State-Province].[Brunswick]    
   }   
  ), {[Geography].[Geography].[Country].[Canada]}   
 )   
ON 0   
FROM [Adventure Works]  
  

```

1月27日 15时 - 1月27日 15时 



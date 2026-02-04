
## 案例说明
多维分析屏蔽维度本维钻取可以通过宏实现，如当选择[商店]维度不能本维度的上钻、下钻，只能钻取到其它维度，屏蔽前后的效果对比如下：
## 实验步骤
1、选择获取需要屏蔽维度本维度钻取的维度名称，在【数据源】中找到对应的多维数据源，再找到对应cube，再找到对应的维度。在对应的维度上右击弹出属性窗口，复制维度名称。以多维数源“Mondrian”下的多维cube“Sales”中的维度[商店]为例。下图是获取[商店]名称的属性窗口图：
2、创建多维分析，在该多维分析中引用[商店]维度，并保存该多维分析。
3、在“分析展现”界面的左侧资源树中，在该多维分析的更多操作菜单中选择 **编辑宏** ：
4、进入宏编辑界面，在报表宏界面新建客户端模块，在弹出的新建模块对话框中选择对象为olapQuery；事件为onRender；
并把下面宏代码复制到代码区域。 
注：步骤1中获取的维度名称要添加到宏代码中的。在宏代码中添加位置如下图：
ClientSide | olapQuery | onRender  
---|---|---  
```
function main(olapQuery) {
    olapQuery.olapTable.restMenuState = function() {
        if (this.e && this.e.target && this.e.target.parentNode && (this.e.target.parentNode.bofclass == "HIERARCHY" || this.e.target.parentNode.bofclass == "LEVEL")) {
            //属性
            this.propertyMemu.setVisibility(true);
            return;
        }
        var uniqueName = this.getCurrentMemberName();
        if (uniqueName.indexOf("BOF_Subtotal") >= 0 || uniqueName.indexOf("BOF_Func_") >= 0) {
            return;
        }
        var hasParent = this._unMapObj[this.tdCurrentMember.getAttribute("un")].at & 1;
        var hasChild = this._unMapObj[this.tdCurrentMember.getAttribute("un")].at & 2;
        // var canCollapse = this.tdCurrentMember.canCollapse == "yes";
        //var hasParent = this.tdCurrentMember.hasParent == "yes";
        //var hasChild = this.tdCurrentMember.hasChild == "yes";
        if (this.tdCurrentMember.getAttribute("lastColumnCell") == "yes") {
            //排序
            this.orderMemu.setVisibility(true);
            this.ascM.setVisibility(true);
            this.descM.setVisibility(true);
            this.bASCM.setVisibility(true);
            this.bDESCM.setVisibility(true);
            this.cancelM.setVisibility(true);
            //过滤
            this.filterMemu.setVisibility(true);
            this.filterCancelM.setVisibility(true);
            this.filterCustomFilterM.setVisibility(true);
            this.filterTopFiveM.setVisibility(true);
            this.filterBottomFiveM.setVisibility(true);
            this.filterTopEightyPerM.setVisibility(true);
            this.filterBottomTwentyPerM.setVisibility(true);
            //属性
            this.propertyMemu.setVisibility(true);
        }
        //下钻
        this.drillMemu.setVisibility(true);
        //修改为对应的维度
        if (this.getCurrentHierarchyName() != "[商店]") {
            this.drillUpM.setVisibility(true);
            this.drillLevelSeparatorM.setVisibility(true);
            this.collapseMemberSeparatorM.setVisibility(true);
            this.drillDownM.setVisibility(true);
            this.drillLevelM.setVisibility(true);
            this.expandMemberM.setVisibility(true);
            this.collapseMemberM.setVisibility(true);
            var memberPath = this.getCurrentMemberPath();
            this.expandPositionM.setVisibility(true);
            this.collapsePositionM.setVisibility(true);
            this.drillToSeparatorM.setVisibility(true);
        }
        this.drillToM.setVisibility(true);
        if (this.tdCurrentMember.getElementsByTagName("SPAN")[0]) {
            if (util.checkFunctionValid("BROWSE_ANALYSISREPORT_SUBTOTAL")) {
                this.subTotalMenu.setVisibility(true);
                this.sumM.setVisibility(true);
                this.avgM.setVisibility(true);
                this.maxM.setVisibility(true);
                this.minM.setVisibility(true);
                this.clearSubTotalSeparatorM.setVisibility(true);
                this.clearSubTotalM.setVisibility(true);
            }
            this.extendMemberMenu.setVisibility(true);
            this.proportionM.setVisibility(true);
            this.rankM.setVisibility(true);
            var hierarchyName = this._hiMap[this._unMapObj[this.tdCurrentMember.getAttribute("un")].hi].n;
            if ((this.isHierarchyOnAxis(0, hierarchyName) && this.isTimeOnAxis(1)) || (this.isHierarchyOnAxis(1, hierarchyName) && this.isTimeOnAxis(0))) {
                this.timeSeparatorM.setVisibility(true);
                this.kibbeeM.setVisibility(true);
                this.chainCompareM.setVisibility(true);
                this.prevValueM.setVisibility(true);
                this.parallelPeriodValueM.setVisibility(true);
                this.parallelPeriodRatioM.setVisibility(true);
                this.prevValueGrowthRateM.setVisibility(true);
                this.periodValueGrowthRateM.setVisibility(true);
            }
            this.clearExtendMemberSeparatorM.setVisibility(true);
            this.clearExtendMemberM.setVisibility(true);
            this.setExtendMemberM.setVisibility(true);
        }
        this.drillUpM.setEnabled(hasParent);
        this.drillDownM.setEnabled(hasChild);
        this.expandMemberM.setEnabled(hasChild);
        this.expandPositionM.setEnabled(hasChild);
        this.collapseMemberM.setEnabled(hasChild);
        this.collapsePositionM.setEnabled(hasChild);
        this.exchangeMenu.setVisibility(true);
        this.drillLevelM.setEnabled(true);
        if (this.tdCurrentMember.getAttribute("lastColumnCell") == "yes") {
            this.hiddenMemu.setVisibility(true);
            this.hiddenColumn.setVisibility(true);
            this.clearColumnHidden.setVisibility(true);
        }
        if (this.tdCurrentMember.getAttribute("lastRowCell") == "yes") {
            this.hiddenMemu.setVisibility(true);
            this.hiddenRow.setVisibility(true);
            this.clearRowHidden.setVisibility(true);
        }
    }
}
```
  

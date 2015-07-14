/**
* JSʵ�ֿɱ༭�ı���
* �÷�:EditTables(tb1,tb2,tb2,......);
* Create by Senty at 2008-04-12
**/

//���ö��������ɱ༭
function EditTables(){
for(var i=0;i<arguments.length;i++){
   SetTableCanEdit(arguments[i]);
}
}

//���ñ����ǿɱ༭��
function SetTableCanEdit(table){
for(var i=1; i<table.rows.length;i++){
   SetRowCanEdit(table.rows[i]);
}
}

function SetRowCanEdit(row){
for(var j=0;j<row.cells.length; j++){

   //������ǰ��Ԫ��ָ���˱༭���ͣ�����ʾ�����༭
   var editType = row.cells[j].getAttribute("EditType");
   if(!editType){
    //������ǰ��Ԫ��û��ָ�������鿴��ǰ���Ƿ�ָ��
    editType = row.parentNode.rows[0].cells[j].getAttribute("EditType");
   }
   if(editType){
    row.cells[j].onclick = function (){
     EditCell(this);
    }
   }
}

}

//����ָ����Ԫ���ɱ༭
function EditCell(element, editType){

var editType = element.getAttribute("EditType");
if(!editType){
   //������ǰ��Ԫ��û��ָ�������鿴��ǰ���Ƿ�ָ��
   editType = element.parentNode.parentNode.rows[0].cells[element.cellIndex].getAttribute("EditType");
}

switch(editType){
   case "TextBox":
    CreateTextBox(element, element.innerHTML);
    break;
   case "DropDownList":
    CreateDropDownList(element);
    break;
   default:
    break;
}
}

//Ϊ��Ԫ�񴴽��ɱ༭������
function CreateTextBox(element, value){
//�����༭״̬�������Ѿ��Ǳ༭״̬������
var editState = element.getAttribute("EditState");
if(editState != "true"){
   //�����ı���
   var textBox = document.createElement("INPUT");
   textBox.type = "text";
   textBox.className="EditCell_TextBox";


   //�����ı�����ǰֵ
   if(!value){
    value = element.getAttribute("Value");
   }
   textBox.value = value;

   //�����ı�����ʧȥ�����¼�
   textBox.onblur = function (){
    CancelEditCell(this.parentNode, this.value);
   }
   //����ǰ��Ԫ�������ı���
   ClearChild(element);
   element.appendChild(textBox);
   textBox.focus();
   textBox.select();

   //�ı�״̬����
   element.setAttribute("EditState", "true");
   element.parentNode.parentNode.setAttribute("CurrentRow", element.parentNode.rowIndex);
}

}


//Ϊ��Ԫ�񴴽�ѡ����
function CreateDropDownList(element, value){
//�����༭״̬�������Ѿ��Ǳ༭״̬������
var editState = element.getAttribute("EditState");
if(editState != "true"){
   //�����½ӿ�
   var downList = document.createElement("Select");
   downList.className="EditCell_DropDownList";

   //�����б���
   var items = element.getAttribute("DataItems");
   if(!items){
    items = element.parentNode.parentNode.rows[0].cells[element.cellIndex].getAttribute("DataItems");
   }

   if(items){
    items = eval("[" + items + "]");
    for(var i=0; i<items.length; i++){
     var oOption = document.createElement("OPTION");
     oOption.text = items[i].text;
     oOption.value = items[i].value;
     downList.options.add(oOption);
    }
   }

   //�����б�ǰֵ
   if(!value){
    value = element.getAttribute("Value");
   }
   downList.value = value;

   //���ô����½ӿ���ʧȥ�����¼�
   downList.onblur = function (){
    CancelEditCell(this.parentNode, this.value, this.options[this.selectedIndex].text);
   }

   //����ǰ��Ԫ�����Ӵ����½ӿ�
   ClearChild(element);
   element.appendChild(downList);
   downList.focus();

   //��¼״̬�ĸı�
   element.setAttribute("EditState", "true");
   element.parentNode.parentNode.setAttribute("LastEditRow", element.parentNode.rowIndex);
}

}


//ȡ����Ԫ���༭״̬
function CancelEditCell(element, value, text){
element.setAttribute("Value", value);
if(text){
   element.innerHTML = text;
}else{
   element.innerHTML = value;
}
element.setAttribute("EditState", "false");

//�����Ƿ��й�ʽ����
CheckExpression(element.parentNode);
}

//����ָ�������������ֽڵ�
function ClearChild(element){
element.innerHTML = "";
}

//������
function AddRow(table, index){
var lastRow = table.rows[table.rows.length-1];
var newRow = lastRow.cloneNode(true);
table.tBodies[0].appendChild(newRow);
SetRowCanEdit(newRow);
return newRow;

}


//ɾ����
function DeleteRow(table, index){
for(var i=table.rows.length - 1; i>0;i--){
   var chkOrder = table.rows[i].cells[0].firstChild;
   if(chkOrder){
    if(chkOrder.type = "CHECKBOX"){
     if(chkOrder.checked){
      //ִ��ɾ��
      table.deleteRow(i);
     }
    }
   }
}
}

//��ȡ������ֵ,JSON��ʽ
function GetTableData(table){
var tableData = new Array();
alert("行数" + table.rows.length);
for(var i=1; i<table.rows.length;i++){
    var chkOrder = table.rows[i].cells[0].firstChild;
    if(chkOrder){
        if(chkOrder.type == 'CHECKBOX'){
            if(chkOrder.checked){
                tableData.push(table.rows[i]);
            }
        }
    }
}

return tableData;

}
//��ȡָ���е����ݣ�JSON��ʽ
function GetRowData(row){
var rowData = {};
for(var j=0;j<row.cells.length; j++){
   name = row.parentNode.rows[0].cells[j].getAttribute("Name");
   if(name){
    var value = row.cells[j].getAttribute("Value");
    if(!value){
     value = row.cells[j].innerHTML;
    }

    rowData[name] = value;
   }
}
//alert("ProductName:" + rowData.ProductName);
//����������alert("ProductName:" + rowData["ProductName"]);
return rowData;

}

//���鵱ǰ����������Ҫ���е��ֶ�
function CheckExpression(row){
for(var j=0;j<row.cells.length; j++){
   expn = row.parentNode.rows[0].cells[j].getAttribute("Expression");
   //��ָ���˹�ʽ��Ҫ������
   if(expn){
    var result = Expression(row,expn);
    var format = row.parentNode.rows[0].cells[j].getAttribute("Format");
    if(format){
     //��ָ���˸�ʽ��������ֵ��ʽ��
     row.cells[j].innerHTML = formatNumber(Expression(row,expn), format);
    }else{
     row.cells[j].innerHTML = Expression(row,expn);
    }
   }

}
}

//������Ҫ�������ֶ�
function Expression(row, expn){
var rowData = GetRowData(row);
//ѭ����ֵ����
for(var j=0;j<row.cells.length; j++){
   name = row.parentNode.rows[0].cells[j].getAttribute("Name");
   if(name){
    var reg = new RegExp(name, "i");
    expn = expn.replace(reg, rowData[name].replace(/\,/g, ""));
   }
}
return eval(expn);
}

///////////////////////////////////////////////////////////////////////////////////
/**
* ��ʽ��������ʾ��ʽ
* �÷�
* formatNumber(12345.999,'#,##0.00');
* formatNumber(12345.999,'#,##0.##');
* formatNumber(123,'000000');
* @param num
* @param pattern
*/
/* �����Ƿ���
formatNumber('','')=0
formatNumber(123456789012.129,null)=123456789012
formatNumber(null,null)=0
formatNumber(123456789012.129,'#,##0.00')=123,456,789,012.12
formatNumber(123456789012.129,'#,##0.##')=123,456,789,012.12
formatNumber(123456789012.129,'#0.00')=123,456,789,012.12
formatNumber(123456789012.129,'#0.##')=123,456,789,012.12
formatNumber(12.129,'0.00')=12.12
formatNumber(12.129,'0.##')=12.12
formatNumber(12,'00000')=00012
formatNumber(12,'#.##')=12
formatNumber(12,'#.00')=12.00
formatNumber(0,'#.##')=0
*/
function formatNumber(num,pattern){
var strarr = num?num.toString().split('.'):['0'];
var fmtarr = pattern?pattern.split('.'):[''];
var retstr='';

// ��������
var str = strarr[0];
var fmt = fmtarr[0];
var i = str.length-1;
var comma = false;
for(var f=fmt.length-1;f>=0;f--){
    switch(fmt.substr(f,1)){
      case '#':
        if(i>=0 ) retstr = str.substr(i--,1) + retstr;
        break;
      case '0':
        if(i>=0) retstr = str.substr(i--,1) + retstr;
        else retstr = '0' + retstr;
        break;
      case ',':
        comma = true;
        retstr=','+retstr;
        break;
    }
}
if(i>=0){
    if(comma){
      var l = str.length;
      for(;i>=0;i--){
        retstr = str.substr(i,1) + retstr;
        if(i>0 && ((l-i)%3)==0) retstr = ',' + retstr;
      }
    }
    else retstr = str.substr(0,i+1) + retstr;
}

retstr = retstr+'.';
// ����С������
str=strarr.length>1?strarr[1]:'';
fmt=fmtarr.length>1?fmtarr[1]:'';
i=0;
for(var f=0;f<fmt.length;f++){
    switch(fmt.substr(f,1)){
      case '#':
        if(i<str.length) retstr+=str.substr(i++,1);
        break;
      case '0':
        if(i<str.length) retstr+= str.substr(i++,1);
        else retstr+='0';
        break;
    }
}
return retstr.replace(/^,+/,'').replace(/\.$/,'');
}

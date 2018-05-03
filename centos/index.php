<!DOCTYPE html>
<html style="height: 100%">
   <head>
       <meta charset="utf-8">
   </head>
   <body style="height: 100%; margin: 0">
   <?php
$servername = "localhost";
$username = "****";
$password = "*******";
$dbname = "****";
$conn = mysqli_connect($servername, $username, $password, $dbname);

if (!$conn) {
    die("连接失败: " . mysqli_connect_error());
}

$wdarr=array();
$sdarr=array();
$mqarr=array();
$sql = "SELECT wendu, shidu, mq FROM bysj";
$result = mysqli_query($conn, $sql);
if (mysqli_num_rows($result) > 0) {
    // 输出数据
    while($row = mysqli_fetch_assoc($result)) {
        echo "wendu: " . $row["wendu"]. "shidu: " . $row["shidu"]. " " . $row["mq"]. "<br>";
	$wdarr[]=$row['wendu'];
	$sdarr[]=$row['shidu'];
	$mqarr[]=$row['mq'];
	
   }
} else {
    echo "0 结果";
}
mysqli_close($conn);

?>
       <div id="container" style="height: 100%"></div>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/echarts.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts-gl/echarts-gl.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts-stat/ecStat.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/extension/dataTool.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/china.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/world.js"></script>
       <script type="text/javascript" src="http://api.map.baidu.com/api?v=2.0&ak=ZUONbpqGBsYGXNIYHicvbAbM"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/extension/bmap.min.js"></script>
       <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/simplex.js"></script>
       <script type="text/javascript">
var dom = document.getElementById("container");
var myChart = echarts.init(dom);
var app = {};
option = null;
option = {
    title: {
        text: '耀民的毕业设计'
    },
    tooltip : {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            label: {
                backgroundColor: '#6a7985'
            }
        }
    },
    legend: {
        data:['温度','湿度','空气']
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis : [
        {
            type : 'category',
            boundaryGap : false,
            data : ['+8','+7','+6','+5','+4','+3','+2','+1']
        }
    ],
    yAxis : [
        {
            type : 'value'
        }
    ],
    series : [
        {
            name:'温度',
            type:'line',
            stack: '℃',
            areaStyle: {normal: {}},
            data:<?php echo json_encode($wdarr);?>
        },
        {
            name:'湿度',
            type:'line',
            stack: '％',
            areaStyle: {normal: {}},
            data:<?php echo json_encode($sdarr);?>
        },
        {
            name:'空气',
            type:'line',
            stack: '％',
            areaStyle: {normal: {}},
            data:<?php echo json_encode($mqarr);?>
        }
        
       
    ]
};
;
if (option && typeof option === "object") {
    myChart.setOption(option, true);
}
       </script>
   </body>
</html>

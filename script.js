var parsed;

function loader(){

$.getJSON("./data3.json",function(data){
    parsed = JSON.parse(data);
    
})

}

var score = [];
var rolls = [];
var gpa = [];
var id = [];
var zero=[];
function makearray(){
    
    var x = 0;
    var i;
    for(i=0;i<parsed.length;i++){
        
        rolls[i] = parsed[i]['name'];
        gpa[i] = parsed[i]['gpa'];
        score[i] = parsed[i]['mark'];
        id[i] = parsed[i]['roll'];
        zero[i] = parsed[i]['zero'];
    }
  
//    console.log(rolls[0]);
//    console.log(gpa[0]);
//    console.log(parsed[0]);
    
}

function alertgpa(name)
{
    var i;
    var div = document.getElementById("rdiv");
    for(i=0;i<rolls.length;i++)
    {
        if(rolls[i]==name)
        {
           div.innerHTML = "Name: "+rolls[i]+"<br><br>"+"Roll: "+id[i]+"<br><br>"+score[i]+"<br>GPA:"+gpa[i] ;
        }
    }
    
    
}
function drawgraph()
{
    document.getElementById("graph").height = window.innerHeight;
    document.getElementById("graph").width = window.innerWidth*2;
    var ctx = document.getElementById("graph").getContext("2d");
    
    var data = {
    labels: rolls,
    datasets: [
        {
            label: "The GPAs of the class",
            fillColor: "rgba(0,0,220,0.5)",
            strokeColor: "rgba(0,0,220,0.8)",
            highlightFill: "rgba(0,0,220,0.75)",
            highlightStroke: "rgba(0,0,220,1)",
            data: gpa
        }
    ]
};

    var myBarChart = new Chart(ctx).Bar(data,{
        scaleBeginAtZero:false,
        scaleOverride:true,
        scaleSteps:10,
        scaleStepWidth:1,
        scaleStartValue: 0
    });
    
    for(var i=0;i<gpa.length;i++)
    {
        if(zero[i]=='true')
        {
            myBarChart.datasets[0].bars[i]['strokeColor']="rgba(220,0,0,0.5)";
            myBarChart.datasets[0].bars[i]['fillColor']="rgba(220,0,0,0.8)";
            myBarChart.datasets[0].bars[i]['highlightFill']="rgba(220,0,0,0.75)";
            myBarChart.datasets[0].bars[i]['highlightStroke']="rgba(220,0,0,1)";
        }
    }
    

    var canvas = document.getElementById("graph");
    canvas.onclick = function(evt){
    var activeBars = myBarChart.getBarsAtEvent(evt);
    alertgpa(activeBars[0]['label']);
    };
}


setTimeout(function(){
    makearray();
    drawgraph(); 
    
     },500);

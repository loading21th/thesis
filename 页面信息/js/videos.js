var i = 0;
var j = 0;
var pname="freevideo-"+i+"-"+j;
var fname="../videos/video-"+i+"-"+j+".mp4";
var iname="../videos/image-"+i+"-"+j+".jpg";
for( i=0; i<2; i++ )
{
    for( j=1; j<7; j++ )
    {
         pname="freevideo-"+i+"-"+j;
         fname="../videos/video-"+i+"-"+j+".mp4";
         iname="../videos/image-"+i+"-"+j+".jpg";
        jwplayer(pname).setup({
            "file": fname,//视频文件路径
        	//"aspectratio": "16:9",//播放器自适应比例
        	"type":"mp4",//播放文件类型（可选）
            "height":"180px",
            "width":"100%",
        	"title": "围棋-业余",//标题（可选）
        	"description": "初学者入门",//描述（可选）
        	"image": iname,//视频封面（可选）
        	"repeat":"false",//重复播放（留空则不重复播放）
        	"autostart":"false",//自动播放（留空则不启用自动播放
        });
    }
}

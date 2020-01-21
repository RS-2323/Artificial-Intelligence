from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return """ <html>
<head>
     <title>Timetable</title>
    <link rel="stylesheet" type="text/css" href="my_timetable.css"/>
    <style type="text/css">
    	#computer{

	border-style: none;
	width: 20%;
	background-color: #BAE6B1;
	color: #7DB979;
	border-radius: .7em;
	padding-left: 10px;
	padding-bottom: 90px;
	


}
#web{

	border-style: none;		
	width: 20%;
	background-color: #B0CFEC;
	color: #84AECE;
	border-radius: .7em;
	padding-left:10px ;
	padding-bottom: 90px;

	}
#web1{

	border-style: none;		
	width: 20%;
	background-color: #B0CFEC;
	color: #84AECE;
	border-radius: .7em;
	padding-left: 10px ;
	padding-bottom: 90px;

}
	#web2{

	border-style: none;		
	width: 20%;
	background-color: #B0CFEC;
	color: #84AECE;
	border-radius: .7em;
	padding-left: 10px;
	padding-bottom:50px;

}

	#data{

	border-style: none;
	width: 20%;
	background-color: #E8AADB;
	color: #A86A9C;
	border-radius: .7em;
	padding-left: 10px;
	padding-bottom:50px ;
		
}
	#data1{
	border-style: none;
	width: 20%;
	background-color: #E8AADB;
	color: #A86A9C;
	border-radius: .7em;
	padding-left: 10px;
	padding-bottom:90px ;

}
	#Project{

	border-style: none;
	width: 20%;
	background-color: #F7F2D4;
	color: #E5DCBA;
	border-radius: .7em;
	padding-left: 10px;
	padding-bottom: 50px;


}
	td {
    border-bottom: 1pt dotted black;
}
.time,#day{
	border-style: none;
}
#table{
	height: 100%;
	width: 80%;
	float: left;


}

#technologyies,#fundamentals,#algorithms,#project1{

	display: none;
}

    </style>
</head>
<body>

  <div >
        <table id="table" cellspacing="20">
            <tbody>
                <tr id="day">
                    <th ></th>
                    <th>Mon<hr></th>
                    <th>Tue<hr></th>
                    <th>Wed<hr></th>
                    <th>Thu<hr></th>
                    <th>Fri<hr></th>
                </tr>
                <tr>
                    <td class="time" >08:00<br><br></td>
                    <td></td>
                    <td></td>
                    <td id="web" rowspan="3">
                        <div >08:15</div>
                        <div >Lecture on Web Technologies</div>
                    </td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td class="time" >09:00<br><br></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td class="time">10:00<br><br></td>
                    <td id="computer" rowspan="3" >
                        <div id >10:15</div>
                        <div >Lecture in Computer Fundamentals</div>
                    </td>
                    <td></td>
                    <td></td>
                    <td id="data" rowspan="2" >
                      <div >10:15</div>
                      <div >Lecture in Algorithms and data structures</div>
                    </td>

                </tr>
                <tr>
                    <td class="time">11:00<br><br></td>
                    <td></td>
                    <td id="project" rowspan="2" >
                        <div >11:15</div>
                        <div >Project 1 Lecture</div>
                    </td>
                    <td></td>
                </tr>
                <tr>
                    <td class="time">12:00<br><br></td>

                    <td id="data1" rowspan="3" >
                        <div >12:15</div>
                        <div >Lecture in Algorithms and data structures</div>
                    </td>
                    <td></TD>
                    <td id="web2" rowspan="2" >
                          <div >12:15</div>
                          <div >Lecture in web technologies</div>
                      </td>
                </tr>

                <tr>
                    <td class="time">13:00<br><br></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>

                <tr>
                    <td class="time">14:00<br><br></td>
                    <td id="web1" rowspan="3" >
                        <div >14:15</div>
                        <div >Lecture in web technologies</div>
                    </td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td class="time">15:00<br><br></td>
                    <td ></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td class="time">16:00<br><br></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td class="time">17:00<br><br></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                   <td></td>
                </tr>
            </tbody>
        </table>
        <p id="para"></p>

        <div style="float: left;">
            <div id="technologyies">
                <h2>Web Technologies</h2>
                <p>In this course the focus is on the World Wide Web as a
                   platform for interactive applications , publication of
                   information and Social services.
               </p>
                <p>Development of web applications require broad knowledge of
                   the underlying technology , formats and standards as the
                   World Wide Web is based and in this topic , you learn about
                   the underlying communication protocol HTTP, markup language
                   HTML, XHTML and XML language for specifying formatting and
                   transformations as CSS and XSLT , event - based programming
                   Client - side and document model DOM , interactive graphics
                   and multimedia content on the web.
               </p>
               <p> The course also provides an introduction to search engines
                   and web index and aspects of content management as
                   standardized descriptions of the content and rules of copyright.
               </p>
               <p>
                   <a href="http://forsk.in/web-development.php" target="_blank">More...</a>
               </p>
            </div>

            <div id="fundamentals">
                <h2 >Computer Fundamentals</h2>
                <p>The course will include terminology, principles and concepts
                   of Construction and operation of various types of modern
                   computers and other computer equipment. Brief historical
                   overview of computer development. Structure ( organization )
                   , functioning and realization of computers and computer
                   systems.
              </p>
              <p>Computer Design on different levels , instruction format,
                   addressing modes , processor architectures and types .
                   Interface between hardware and software, linking components,
                   interruptions , buses , inventory hierarchy and cache
                   ( Eng . cache). Review of key computer technology devices
                   ( peripheral devices) .
               </p>
               <p>Brief introduction to distributed systems , embedded
                 ( "embedded " ) systems , parallel computers ,
                 new technologies and new applications ( apps) .
               </p>
               <p>
                   <a href="http://forsk.in/computer-science-fundamentals.php" target="_blank">More...</a>
               </p>
            </div>

            <div id="algorithms">
                <h2>Algorithms and data structures</h2>
                <p>Methods for analyzing the efficiency of algorithms, splitter
                  and Conquer techniques , recursive solution methods.
                  Methods for ordering , searching and sorting of data.
                  Data structures for effective retrieval of data ,
                  dynamic programming and greed algorithms.
               </p>
               <p>Data structures for the creation of graphs and networks ,
                 as well as methods for through running and exploration.
                 Algorithms for finding the best path (s) and couplings
                 ( matchings ) , spanning trees and maximum flow . theory
                  problem complexity.
               </p>
               <p>Algorithms are expressed in language independent .
               </p>
               <p>
                   <a href="http://forsk.in/industrial-c-programming.php" target="_blank">More ...</a>
               </p>
            </div>

            <div id="project1">
                <h2>Project 1</h2>
                <p>Knowledge of methods and theories of organization of
                  group programming projects. Understanding the interplay
                  between process and product -oriented challenges and
                  activities in a programming project.
               </p>
               <p>Practical skills in programming and integration of various
                  components to assemble a larger software product.
               </p>
               <p>Have skills in teamwork and can reflect on both technical
                  and organizational aspects of a programming project .
               </p>
               <p>
                   <a href="http://forsk.in/iot.php" target="_blank">More...</a>
               </p>
            </div>
        </div>
 
        
    </div>
    
            <script>
                document.getElementById("web").addEventListener("mouseover", myFunction1);
                document.getElementById("web").addEventListener("mouseout", myFunction2);
                function myFunction1(){
                    document.getElementById("para").innerHTML=technologyies.innerHTML;
                }
                function myFunction2(){
                    document.getElementById("para").innerHTML=" ";
                }




                document.getElementById("web1").addEventListener("mouseover", myFunction3);
                document.getElementById("web1").addEventListener("mouseout", myFunction4);
                function myFunction3(){
                    document.getElementById("para").innerHTML=technologyies.innerHTML;
                }
                function myFunction4(){
                    document.getElementById("para").innerHTML=" ";
                }



                document.getElementById("web2").addEventListener("mouseover", myFunction5);
                document.getElementById("web2").addEventListener("mouseout", myFunction6);
                function myFunction5(){
                    document.getElementById("para").innerHTML=technologyies.innerHTML;
                }
                function myFunction6(){
                    document.getElementById("para").innerHTML=" ";
                }






                document.getElementById("computer").addEventListener("mouseover", myFunction7);
                document.getElementById("computer").addEventListener("mouseout", myFunction8);
                function myFunction7(){
                    document.getElementById("para").innerHTML=fundamentals.innerHTML;
                }
                function myFunction8(){
                    document.getElementById("para").innerHTML=" ";
                }






                document.getElementById("data").addEventListener("mouseover", myFunction9);
                document.getElementById("data").addEventListener("mouseout", myFunction10);
                function myFunction9(){
                    document.getElementById("para").innerHTML=algorithms.innerHTML;
                }
                function myFunction10(){
                    document.getElementById("para").innerHTML=" ";
                }




                document.getElementById("data1").addEventListener("mouseover", myFunction11);
                document.getElementById("data1").addEventListener("mouseout", myFunction12);
                function myFunction11(){
                    document.getElementById("para").innerHTML=algorithms.innerHTML;
                }
                function myFunction12(){
                    document.getElementById("para").innerHTML=" ";
                }
                            


                document.getElementById("project").addEventListener("mouseover", myFunction13);
                document.getElementById("project").addEventListener("mouseout", myFunction14);
                function myFunction13(){
                    document.getElementById("para").innerHTML=project1.innerHTML;
                }
                function myFunction14(){
                    document.getElementById("para").innerHTML=" ";
                }

</script>
</body>
</html>


"""



if __name__ == '__main__':
    app.run()
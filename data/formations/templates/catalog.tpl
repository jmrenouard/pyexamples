<!DOCTYPE html>
<html>
<head>    
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Catalogue de formation">
    <meta name="author" content="Jean-Marie Renouard - LightPath 2018&copy;">
    <!-- <meta http-equiv="refresh" content="2" > -->
	<title>Catalogue de formation</title>
	  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.bundle.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  
</head>
<body>
      <h1>Catalogue de formation</h1>
      <ul class="nav nav-tabs">
        {% for training in trainings %}
            
            <li {% if loop.index == 1 %}class='active'{% endif %}><a data-toggle="tab" href="#training{{loop.index}}">{{training.title}}</a></li>
        {% endfor %}
      </ul>
     <div class="tab-content">
    {% for training in trainings %}
        <div id="training{{loop.index}}" class="tab-pane fade {% if loop.index == 1 %}in active{% endif %}">
    <!--
        <pre>
            {{training|pprint}}
        </pre>
    -->
    <h1>{% if training.logo %}<img src="{{training.logo}}"/>{% endif %}{{training.title|e}}</h1>
    <hr>
    <div class="well">
    	<div class="row">
    		<div class="col-sm-6">
    		 	<h3><p class="fas fa-cogs fa-1x"></p>Objectifs:</h3>
    			<ul>
    			{% for obj in training.objectives %}
    				<li>{{obj|e}}</li>
    			{% endfor %}
    			</ul>
    		</div>
    		<div class="col-sm-6">
    			<h3><p class="fas fa-clipboard-list"></p>M&eacute;thodologie:</h3>
    			<ul>
    			{% for obj in training.methodologies %}
    				<li>{{obj|e}}</li>
    			{% endfor %}
    			</ul>
    		</div>
    	</div>
    	<div class="row">
    		<div class="col-sm-6">
    			<h3><p class="far fa-clock"></p>Dur&eacute;e: {{training.duration|e}}</h3>
    			{% if training.certification %}
    			<h3><p class="fas fa-user-graduate"></p>Certification: {{training.certification|e}}</h3>
    			{% endif %}
    		</div>
    		<div class="col-sm-6">
    			<h3><p class="fas fa-thumbtack"></p>Pr&eacute;requis:</h3>
    			<ul>
    			{% for obj in training.requirements %}
    				<li>{{obj|e}}</li>
    			{% endfor %}
    			</ul>

    			<h3><p class="fas fa-users"></p>Public:</h3>
    			<ul>
    			{% for obj in training.publics %}
    				<li>{{obj|e}}</li>
    			{% endfor %}
    			</ul>
    		</div>
    	</div>
    </div>

    <h1><p class="fas fa-tasks fa-2x"></p>Programme</h1>
    <hr/>
    <!--
    <pre>
    {{training.modules|pprint}}
    </pre>
    -->
    {% set colChanged=False %} 
    <div class="row">
    	<div class="col-sm-6">
    	{% for mod in training.modules %}
            <h3 class='well'>
                <span class="fa-stack fa-1x">
                    <i class="fa fa-circle fa-stack-2x"></i>
                    <strong class="fa-stack-1x text-primary">{{loop.index}}</strong>
                </span>
                {{mod.module|e}}
            </h3>
            <ul>
            {% for itm in mod.elements %}
                <li>{{itm|e}}</li>
            {% endfor %}
            </ul>
    		
    		{% if 
                (
                 (loop.length % 2==0 and loop.index % ((loop.length/2))==0.0) 
                   or 
                 (loop.length % 2==1 and loop.index % (0.5+(loop.length/2)) ==0) 
                 )
            %}
    			</div>
    			<div class="col-sm-6">
    		{% endif %}
    	{% endfor %}
    	</div>
    </div>
    </div>
    {% endfor %}
<hr/>
<div class='footer row'>
    <div class='col-sm-4'>
    <img src="lightpath.jpeg"/>
    </div>
​   <div class='col-sm-2'>
    SIRET:    75048152500012<br/>
    RCS :     Rennes B 750 481 525
    </div>
   <div class='col-sm-2'>
Adresse: 27, allée Jean Monnet<br/>
              35340 La Bouëxière
    </div>
<div class='col-sm-4'>
Mobile :  +33 (0)6 62 69 58 81<br/>
Email :    jmrenouard@lightpath.fr
    </div>
</div>
</body>
</html>
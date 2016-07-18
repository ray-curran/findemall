'use strict';

angular.module('AngularFlask', ['angularFlaskServices', 'uiGmapgoogle-maps'])
	.config(['$routeProvider', '$locationProvider', 'uiGmapGoogleMapApiProvider',
		function($routeProvider, $locationProvider, uiGmapGoogleMapApiProvider) {
    uiGmapGoogleMapApiProvider.configure({
         //    key: 'your api key',
         v: '3.20', //defaults to latest 3.X anyhow
         libraries: 'weather,geometry,visualization'
     });

    $routeProvider
    .when('/', {
      templateUrl: 'static/partials/testing.html',
      controller: TestController
    })
    .otherwise({
      redirectTo: '/'
    })
    ;


		$locationProvider.html5Mode(true);

	}])

;
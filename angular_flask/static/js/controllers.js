'use strict';

/* Controllers */

function TestController($scope, $http) {
  // var pokemonQuery = testing.get({}, function(tests) {
  //   $scope.pokemon = tests;
  // });

  $scope.loading = true;

  $http.get('/api/testing').success(function(data) {
    $scope.pokemon = data.pokemon_close;
    $scope.loading = false;
    $scope.tryagain = false;
  }).error(function(data) {
    $scope.loading = false;
    $scope.tryagain = true;
  })

}

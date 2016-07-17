'use strict';

angular.module('angularFlaskServices', ['ngResource'])
  .factory('testing', function($resource) {
    return $resource('/api/testing', {}, {
      query: {
        method: 'GET'
      }
    });
  })
;




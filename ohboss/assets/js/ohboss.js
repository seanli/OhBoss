angular.module('fundstrap', ['firebase']).
controller('Chat', ['$scope', '$timeout', 'angularFireCollection',
  function($scope, $timeout, angularFireCollection) {
    var el = document.getElementById("messagesDiv");
    var url = 'https://fundstrap.firebaseio.com';
    $scope.messages = angularFireCollection(url, function() {
      $timeout(function() { el.scrollTop = el.scrollHeight; });
    });
    $scope.username = 'Guest' + Math.floor(Math.random()*101);
    $scope.addMessage = function() {
      $scope.messages.add({from: $scope.username, content: $scope.message}, function() {
        el.scrollTop = el.scrollHeight;
      });
      $scope.message = "";
    }
  }
]);

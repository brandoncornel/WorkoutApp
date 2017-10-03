workouts.controller('WorkoutController', function($scope, Workouts, Excercises, Sessions, Sets, Users) {
        Users.query().$promise.then(function(data){
        	$scope.users = data
        });

        $scope.createUser = function(){
        	Users.save('{"name":"CORNEL","weight":200000}')
        }

        
});
workouts.controller('WorkoutController', function($scope, Workouts, Excercises, Sessions, Sets, Users) {
        Users.query().$promise.then(function(data){
        	$scope.users = data
        });

        
});
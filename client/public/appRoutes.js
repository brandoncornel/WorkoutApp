angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

    $stateProvider.state({
        name: 'workouts',
        url: '/',
        templateUrl: 'public/components/workouts/templates/workouts.template',
        controller: 'WorkoutController'
    });

    $urlRouterProvider.otherwise('/');
}]);
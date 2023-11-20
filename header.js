/*<![CDATA[*/

var app = angular.module( "portfolioSite", [] );
app.controller( "headerCtrl", function( $scope, $http, $q ) {

    $scope.setup = function() {

        if ( $scope.title == 'Home' ) {

            $scope.nav_menu_components = {
                'Home' : './index.html',
                'Programming Projects' : './programming-projects/programming-projects.html',
                'Nick' : './nick/nick.html'
            }

        } else {

            $scope.nav_menu_components = {
                'Home' : '../index.html',
                'Programming Projects' : '../programming-projects/programming-projects.html',
                'Nick' : '../nick/nick.html'
            }

        }

        $scope.nav_menu_components[ $scope.title ] = '#';

    };

    $scope.title = 'Programming Projects'

    $scope.setup();

});

/*]]>*/

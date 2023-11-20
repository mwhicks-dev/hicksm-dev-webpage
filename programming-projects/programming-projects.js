/*<![CDATA[*/

app.controller( "programmingProjectsCtrl", function( $scope, $http, $q ) {

    $scope.debug = 0;

    /* Variables */

    $scope.active_projects_flag = '[ACTV]';
    $scope.inactive_projects_flag = '[COMP]';

    $scope.profiles = [
        { 'root' : 'https://api.github.com', 'username' : 'mwhicks-dev', 'headers' : { 'Authorization' : 'token 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' } },
        { 'root' : 'https://api.github.ncsu.edu', 'username' : 'mwhicks2', 'headers' : { 'Authorization' : 'token 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' } },
    ]; /* EXPIRES: MM/DD/YYYY */
    $scope.active_projects = [];
    $scope.inactive_projects = [];

    /* Functions */

    $scope.processProfile = function( profile ) {

        if ( $scope.debug > 0 ) {
            console.log( "-> processProfile" );
            console.log( "Profile:" );
            console.log( profile );
        }

        $http({
            method : 'GET',
            url : profile[ 'root' ] + '/users/' + profile[ 'username' ] + '/repos',
            headers : profile[ 'headers' ]
        }).then( function( response ) { $scope.processRepositories( response.data, profile ); } );

        if ( $scope.debug > 0 ) {
            console.log( "<- processProfile" );
        }

    };

    $scope.processRepositories = function( repositories, profile ) {

        $scope.ctr++;

        if ( $scope.debug > 0 ) {
            console.log( "-> processRepositories" );
            console.log( "Repositories:" );
            console.log( repositories );
        }

        for ( let i in repositories ) {
            let repository = repositories[ i ];
            if ( repository[ 'description' ] != null && repository[ 'description' ].length > 6
                    && ( repository[ 'description' ].substring( 0, 6 ) == $scope.active_projects_flag
                    || repository[ 'description' ].substring( 0, 6 ) == $scope.inactive_projects_flag ) ) {

                $scope.processRepository( repository, profile );

            }
        }

        if ( $scope.debug > 0 ) {
            console.log( "<- processRepositories" );
        }

    };

    $scope.processRepository = function( repository, profile ) {

        if ( $scope.debug > 0 ) {
            console.log( "-> processRepository" );
            console.log( "Repository:" );
            console.log( repository );
        }

        // Get basic repository data
        let repository_data = {
            'name' : repository.name,
            'description' : repository.description,
            'website' : repository.homepage,
            'github_website' : repository.html_url
        };

        // Get further HTTP data
        $scope.processPullRequests( repository, repository_data, profile );
        $scope.processLanguages( repository, repository_data, profile );

        // Push repository data reference to project lists
        if ( repository_data[ 'description' ].substring( 0, 6 ) == $scope.active_projects_flag ) {
            $scope.active_projects.push( repository_data );
        } else {
            $scope.inactive_projects.push( repository_data );
        }

        if ( $scope.debug > 1 ) {
            console.log( 'Repository data:' );
            console.log( repository_data );
        }

        if ( $scope.debug > 0 ) {
            console.log( "<- processRepository" );
        }

    };

    $scope.processPullRequests = function( repository, data, profile ) {

        if ( $scope.debug > 1 ) {
            console.log( "-> processPullRequests" );
        }

        data[ 'pull_request' ] = null;

        // Get repository pull requests
        $http({
            method : 'GET',
            url : repository.url + '/pulls?state=closed',
            headers : profile.headers
        }).then( function( response ) {

            if ( $scope.debug > 1 ) {
                console.log( 'Pull requests:' );
                console.log( response.data );
            }

            if ( response.data.length > 0 ) {

                for ( let i in response.data ) {

                    let pull_request = response.data[ i ];

                    // Continue if not merged into production
                    if ( !pull_request.hasOwnProperty( 'merged_at' )
                            || pull_request[ 'merged_at' ] == null
                            || pull_request[ 'base' ][ 'ref' ] != 'main' ) { continue; }

                    // Otherwise, actually mark pull request and break
                    data[ 'pull_request' ] = {
                        'name' : pull_request.title,
                        'description' : pull_request.body
                    };

                    break;

                }

            }

        });

        if ( $scope.debug > 1 ) {
            console.log( "<- processPullRequests" );
        }

    }

    $scope.processLanguages = function( repository, data, profile ) {

        if ( $scope.debug > 1 ) {
            console.log( "-> processLanguages" );
        }

        data[ 'languages' ] = null;

        // Get repository languages
        $http({
            method : 'GET',
            url : repository.url + '/languages',
            headers : profile.headers
        }).then( function ( response ) {

            if ( $scope.debug > 1 ) {
                console.log( 'Languages:' );
                console.log( response.data );
            }

            if ( Object.keys( response.data ).length > 0 ) {
                data[ 'languages' ] = response.data;
            }

            $scope.fixProjectLanguages( data[ 'languages' ] );

        });

        if ( $scope.debug > 1 ) {
            console.log( "<- processLanguages" );
        }

    }

    $scope.fixProjectLanguages = function( languages ) {

        if ( languages == null ) { return; }

        // Get language keys
        const keys = Object.keys( languages );

        // Get total amount of lines
        let total = 0;
        for ( let i in keys ) {
            total += parseInt( languages[ keys[ i ] ] );
        }

        // Convert each lines to percentage
        for ( let i in keys ) {
            languages[ keys[ i ] ] = 1.0 * parseInt( languages[ keys[ i ] ] ) / total * 100;
        }

        // Convert each percentage to string
        for ( let i in keys ) {
            if ( languages[ keys[ i ] ] < 1 ) {
                languages[ keys[ i ] ] = "<1";
            } else {
                languages[ keys[ i ] ] = parseInt( languages[ keys[ i ] ] ).toString();
            }
        }

    }

    // Process profiles
    for ( let i in $scope.profiles ) {

        $scope.processProfile( $scope.profiles[ i ] );

    }

});

/*]]>*/

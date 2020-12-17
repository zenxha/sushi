if ( ! is_user_logged_in() && isset( $_GET[ 'fl_builder' ] ) ) {
  auth_redirect();
}
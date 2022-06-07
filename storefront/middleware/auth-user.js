export default async function ({ $auth, redirect, store }) {
    let user = $auth.loggedIn;
    if (!$auth.loggedIn) {


        redirect('/auth')
    
}
}
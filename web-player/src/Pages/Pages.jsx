import Home from './Home/Home.jsx'
import Login from './Login/Login.jsx'
import Registration from './Registration/Registration.jsx';
import ResetPassword from './ResetPassword/ResetPassword.jsx';
import NewPassword from './NewPassword/NewPassword.jsx';

export const HomePage = (id) => Home(id);
export const LoginPage = () => Login();
export const RegistrationPage = () => Registration();
export const ResetPasswordPage = () => ResetPassword();
export const NewPasswordPage = () => NewPassword();
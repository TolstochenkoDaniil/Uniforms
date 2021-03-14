import { createStore } from 'vuex';
import disciplines from './modules/disciplines.store';
import university from './modules/university.store';
import forms from './modules/forms.store';
import form from './modules/form.store';
import auth from './modules/auth.store';

const store = createStore({
     modules: {
          university,
          disciplines,
          forms,
          form,
          auth,
     }
});

export default store;
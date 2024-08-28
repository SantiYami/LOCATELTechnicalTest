import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import { ValidationProvider, ValidationObserver, extend, localize, localeChanged} from 'vee-validate';
import * as rules from 'vee-validate/dist/rules';
import es from 'vee-validate/dist/locale/es.json';
import en from 'vee-validate/dist/locale/en.json';
import VueI18n from 'vue-i18n'
import messages from './i18n'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";

import '@/stylessheets/style.scss'

//* TOAST OPTIONS
const options = {
  position: "bottom-center",
  timeout: 5000,
  closeOnClick: true,
  pauseOnFocusLoss: true,
  pauseOnHover: true,
  draggable: true,
  draggablePercent: 0.6,
  showCloseButtonOnHover: false,
  closeButton: "button",
  icon: true,
  rtl: false
};

Vue.use(Toast, options);

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)


Vue.config.productionTip = false

Vue.use(VueI18n)

const i18n = new VueI18n({
  locale: 'es', // set locale
  messages, // set locale messages
  silentTranslationWarn: true
})

localize({
  es,
  en
});
localize('es');
localeChanged();

Object.keys(rules).forEach(rule => {
  extend(rule, {
    ...rules[rule]// copies rule configuration
  });
});

Vue.component("ValidationObserver", ValidationObserver);
Vue.component("ValidationProvider", ValidationProvider);

new Vue({
  router,
  store,
  i18n,
  components: {
    ValidationProvider
  },
  render: h => h(App)
}).$mount('#app')

import i18next from "i18next";
import Backend from "i18next-http-backend";
import LanguageDetector from "i18next-browser-languagedetector";
import { initReactI18next } from "react-i18next";

i18next
  .use(Backend) // Carga los archivos JSON
  .use(LanguageDetector) // Detecta el idioma del navegador
  .use(initReactI18next) // Integración con React
  .init({
    fallbackLng: "en", // Idioma predeterminado
    debug: true, // Activa logs para depuración
    backend: {
      loadPath: "/locales/{{lng}}.json", // Ruta a los archivos JSON
    },
    interpolation: {
      escapeValue: false, // No escapar valores HTML
    },
  });

export default i18next;
from abc import ABC, abstractmethod


class QualityLoop(ABC):
    """
    x_train: Anlagenparameter, Merkmale (Features) z.B. Sensordaten
    y_train: Zielvariable Qualitätsdaten z.B. KMG-Messdaten
    """
    @abstractmethod
    def load_data(self):
        """
        Merkmale (features) aus Zeitreihen müssen erstellt/ extrahiert werden
            --> Anomalien/ Ausreißer erkennen/ filtern
        wo kommen Daten her - aus AAS?
        return: x_train, y_train, x_test, y_test
        """
        pass

    @abstractmethod
    def train_model(self, x_train, y_train):
        """
        Model trainieren
        return: model
        """
        pass

    @abstractmethod
    def evaluate_model(self, model, x_test, y_test):
        """
        Model bewerten
        """
        pass

    @abstractmethod
    def generate_new_plant_parameters(self, model, AAS):
        """
        wann ausgelöst? wenn Qualitätsdaten WarningLimit erreicht?
        Merkmale (features) aus Zeitreihen müssen erstellt/ extrahiert werden
            --> Anomalien/ Ausreißer erkennen/ filtern
            --> auf AAS gespeichert; post_request
        get_request für aktuelle Anlagenparameter, Qualitätsdaten
        post_request für neue Anlagenparameter; neue Anlagenparameter müssen Maschine übergeben werden
        """
        pass

    @abstractmethod
    def evaluate_new_plant_parameter(self, new_plant_parameters, quality_data_for_new_plant_parameters):
        """
        Funktion soll die in generate_new_plant_parameters generierten Anlagenparameter mit Qualitätsdaten
        z.B. KMG-Messdaten testen und das Model weiter trainieren/ stetig verbessern --ist das möglich??
        """
        pass
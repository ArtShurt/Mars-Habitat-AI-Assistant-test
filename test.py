import random
from datetime import datetime, timedelta

class ResourceMonitor:
    def __init__(self, name, critical_threshold):
        self.name = name
        self.level = 100  # Nivel inicial (puede ajustarse)
        self.critical_threshold = critical_threshold
        self.log = []

    def update_level(self):
        """Simula una actualización del nivel del recurso (por ejemplo, un cambio cada hora)."""
        self.level -= random.uniform(0.5, 2.0)  # Decremento aleatorio para simular consumo

    def check_critical(self):
        """Verifica si el recurso ha caído bajo el umbral crítico."""
        if self.level < self.critical_threshold:
            print(f"Warning: {self.name} level is critically low ({self.level}%)!")
            return True
        return False

    def log_data(self):
        """Registra el nivel de recurso actual con una marca de tiempo."""
        self.log.append((datetime.now(), self.level))

    def predict_future_levels(self, hours_ahead=1):
        """Predice el nivel del recurso basado en el historial de consumo."""
        # Este es un modelo simple. Podríamos mejorar con Machine Learning.
        avg_consumption = sum([self.log[i][1] - self.log[i - 1][1] for i in range(1, len(self.log))]) / len(self.log)
        predicted_level = self.level + avg_consumption * hours_ahead
        return max(0, predicted_level)  # No puede ser negativo


class MarsHabitatAI:
    def __init__(self):
        self.temperature_monitor = ResourceMonitor("Temperature", 15)  # Umbral crítico: 15%
        self.oxygen_monitor = ResourceMonitor("Oxygen", 20)           # Umbral crítico: 20%
        self.energy_monitor = ResourceMonitor("Energy", 10)           # Umbral crítico: 10%

    def monitor_resources(self):
        """Monitorea todos los recursos y emite alertas si están en niveles críticos."""
        print("Monitoring resources...")
        self.temperature_monitor.update_level()
        self.oxygen_monitor.update_level()
        self.energy_monitor.update_level()

        if self.temperature_monitor.check_critical():
            print("Action needed: Adjust temperature systems.")
        if self.oxygen_monitor.check_critical():
            print("Action needed: Increase oxygen supply.")
        if self.energy_monitor.check_critical():
            print("Action needed: Optimize energy usage.")

    def log_all_data(self):
        """Registra los datos de todos los recursos."""
        self.temperature_monitor.log_data()
        self.oxygen_monitor.log_data()
        self.energy_monitor.log_data()

    def predict_all_levels(self):
        """Proporciona predicciones para todos los recursos."""
        print("Predicted levels in 1 hour:")
        print(f"Temperature: {self.temperature_monitor.predict_future_levels()}%")
        print(f"Oxygen: {self.oxygen_monitor.predict_future_levels()}%")
        print(f"Energy: {self.energy_monitor.predict_future_levels()}%")

# Ejemplo de uso
if __name__ == "__main__":
    ai_assistant = MarsHabitatAI()

    # Simulación simple
    for _ in range(5):  # Simula 5 horas
        ai_assistant.monitor_resources()
        ai_assistant.log_all_data()
        ai_assistant.predict_all_levels()
        print("-" * 50)
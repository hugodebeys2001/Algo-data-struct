class Solution:

    # Function to find starting point where the truck can start to get through
    # the complete circle without exhausting its petrol in between.
    def tour(self, lis, n):
        total_petrol = 0
        start_index = 0
        current_petrol = 0

        for i in range(n):
            petrol, distance = lis[i]
            total_petrol += petrol - distance
            current_petrol += petrol - distance

            # Si la quantité de carburant devient négative, cela signifie que le camion ne peut pas atteindre
            # la station-service suivante en partant de la station actuelle
            if current_petrol < 0:
                # Réinitialiser la station de départ à la suivante
                start_index = i + 1
                current_petrol = 0

        # Si le total du carburant disponible est positif, cela signifie qu'il existe une solution
        # Sinon, il n'y a pas de solution
        if total_petrol >= 0:
            return start_index
        else:
            return -1
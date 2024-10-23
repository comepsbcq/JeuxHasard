using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.ConstrainedExecution;
using System.Text;
using System.Threading.Tasks;
using System.Security.Policy;

namespace Aléatoire
{
    internal class Program
    {
        static string[] valeurs = { "0", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10" };
        static Random rand = new Random();
        static void Main(string[] args)
        {
            start();
        }
        // Variable pour les couleurs de la console
        static ConsoleColor VERT = ConsoleColor.Green;
        static ConsoleColor ROUGE = ConsoleColor.Red;
        static ConsoleColor JAUNE = ConsoleColor.Yellow;
        static ConsoleColor BLEU = ConsoleColor.Blue;
        static ConsoleColor RESET = ConsoleColor.White;

        static void RejouerDES()
        {
            Console.WriteLine("Souhaitez-vous rejouer ou retourner au menu ? (Rejouer/menu)");
            string rejouer = Console.ReadLine().ToLower();
            if (rejouer == "rejouer")
            {
                des();
            }
            else if (rejouer == "menu")
            {
                start();
            }
            else
            {
                Console.WriteLine("Erreur de syntaxe : veuillez entrer une des options disponibles.");
                RejouerDES();
            }
        }

        static void RejouerPF()
        {
            Console.WriteLine("Souhaitez-vous refaire un tirage ou retourner au menu ? (Rejouer/menu)");
            string rejouer = Console.ReadLine().ToLower();
            if (rejouer == "rejouer")
            {
                pf();
            }
            else if (rejouer == "menu")
            {
                start();
            }
            else
            {
                Console.WriteLine("Erreur de syntaxe : veuillez entrer une des options disponibles.");
                RejouerPF();
            }
        }

        static void RejouerMM()
        {
            Console.WriteLine("Souhaitez-vous rejouer ou retourner au menu ? (Rejouer/menu)");
            string rejouer = Console.ReadLine().ToLower();
            if (rejouer == "rejouer")
            {
                //Mastermind();
            }
            else if (rejouer == "menu")
            {
                start();
            }
            else
            {
                Console.WriteLine("Erreur de syntaxe : veuillez entrer une des options disponibles.");
                RejouerMM();
            }
        }

        // Fonction lancer de dés
        static void des()
        {
            Console.Clear();
            Console.WriteLine("Bienvenue dans le lancer de dés !\nCombien de fois voulez-vous que le dé soit lancé ?");
            int nbDes = int.Parse(Console.ReadLine());
            for (int i = 0; i < nbDes; i++)
            {
                int resultat = rand.Next(1, 7);
                Console.WriteLine("Votre lancer a donné : " + resultat);
            }
            RejouerDES();
        }
        static void pf()
        {
            Console.Clear();
            Console.WriteLine("Bienvenue au Pile ou Face !");
            Console.WriteLine("Choisissez votre pari : ");
            string pari = Console.ReadLine().ToLower();
            int x = rand.Next(0,1000);
            if (pari == "pile")
            {
                if (x > 500) { Console.WriteLine("Le tirage a donné pile. Bravo !"); Console.ReadLine(); }
                else { Console.WriteLine("Le tirage a donné face. Dommage."); Console.ReadLine(); }
            }
            else if (pari == "face")
            {
                if (x > 500) { Console.WriteLine("Le tirage a donné pile. Dommage !"); Console.ReadLine(); }
                else { Console.WriteLine("Le tirage a donné face. Bravo !"); Console.ReadLine();  }
            }
            else { Console.WriteLine("Synthax error : please type a correct answer."); Console.ReadLine(); pf(); }
        }
        static void BlackJack()
        {
            Console.Clear();
            Console.WriteLine("Bienvenue au BlackJack !\nCe jeu fonctionne comme au casino, c'est à dire avec des jetons limités (en cas de perte totale des jetons, ils vous seront remis à zéro).");
            Console.WriteLine("Attention : jouer peut entraîner des RISQUES D'ADDICTION.");
            Console.WriteLine("Voulez-vous continuer ? (oui/non)");
            string userChoice = Console.ReadLine().ToLower();
            if (userChoice == "oui")
            {
                Console.Clear();
                Console.WriteLine("Pour rappeler les règles : vous commence avec deux cartes. Celle-ci ont une valeur allant de 2 à 11. L'intégralité des cartes possèdent la valeur écrite dessus, mis à part le valet, la dame, le roi qui valent 10 et l'as qui vaut 11 ou 1 en fonction du contexte. Vous pouvez choisir de vous retirer, ou de repiocher une carte. Si la valeur totale de vos cartes dépassent 21, vous avez perdu. Cependant, vous devez faire en sorte de dépasser le croupier, qui joue selon les mêmes principes.");
                Console.WriteLine("Appuyez sur une touche pour continuer...");
                Console.ReadKey();
                Console.Clear();
                bool boucle = true;
                int valeur = rand.Next(2, 12) + rand.Next(2, 12);
                int valeurBOT = rand.Next(2, 12) + rand.Next(2, 12);
                while (boucle)
                {
                    Console.WriteLine($"Votre valeur est de {valeur}, et celle du croupier est de {valeurBOT}.");
                    Console.WriteLine("Souhaitez vous prendre une carte ou s'arrêter là ? (prendre/stop)");
                    string pickornot = Console.ReadLine().ToLower();
                    if (pickornot == "prendre")
                    {
                        int carte = rand.Next(2, 12);
                        if (valeur + carte > 21 && carte == 11) carte = 1;
                        valeur += carte;
                    }
                    else if (pickornot == "stop")
                    {
                        while (valeurBOT < 17)
                        {
                            int carteBOT = rand.Next(2, 12);
                            valeurBOT += carteBOT;
                            Console.WriteLine($"La valeur du croupier est de {valeurBOT}");
                        }
                        boucle = false;
                    }
                }
                // Vérification des résultats
                if (valeur > 21) { Console.WriteLine($"Perdu ! Votre valeur a dépassé 21 en atteignant : {valeur}"); Console.ReadLine(); }
                else if (valeurBOT > 21 || valeur > valeurBOT) { Console.WriteLine($"Bravo ! Vous avez gagné ! Votre valeur est de {valeur}, et celle du croupier et de {valeurBOT}"); Console.ReadLine(); }
                else if (valeurBOT > valeur) { Console.WriteLine($"Perdu ! Votre valeur est inférieur à celle du croupier !"); Console.ReadLine(); }
                Console.WriteLine("Souhaitez-vous rejouer ? (oui/non)");
                string rejouer = Console.ReadLine().ToLower();
                if (rejouer == "oui") { BlackJack(); }
                else if (rejouer == "non") { start(); }
            }
            else if (userChoice == "non") { start(); }
            else { Console.WriteLine("Synthax error: please type a correct answer."); Console.ReadLine(); }
        }
        static void start()
        {
            // Affichage de la présentation
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("Bienvenue au jeu de l'aléatoire !");
            Console.WriteLine("Ce programme vous permet de jouer à différents jeux d'aléatoires comme le pile ou face, les lancés de dés, etc...");
            Console.WriteLine("Ce programme a été développé par Côme PASBECQ");
            // Liste des choix
            Console.WriteLine("Veuillez faire votre choix parmis les suivants :");
            Console.WriteLine("  - Pile ou face (1)");
            Console.WriteLine("  - Lancer de dé (2)");
            Console.WriteLine("  - Blackjack (3)");
            Console.WriteLine("  - MasterMind (4)");
            Console.WriteLine("  - Fermer le programme (5)");
            // Lire le choix de l'utilisateur
            Console.WriteLine("Votre choix (uniquement le chiffre associé");
            string input = Console.ReadLine();
            int userChoice;

            // Vérification de l'entrée
            if (int.TryParse(input, out userChoice))
            {
                // Exécuter la fonction correspondant au choix de l'utilisateur
                switch (userChoice)
                {
                    case 1:
                        pf();
                        break;
                    case 2:
                        des();
                        break;
                    case 3:
                        BlackJack();
                        break;
                    case 4:
                        //Mastermind();
                        break;
                    case 5:
                        Console.WriteLine("Fermeture du programme.");
                        Console.ReadKey();  // Pause avant de fermer
                        return;
                    default:
                        Console.WriteLine("Erreur de syntaxe : valeur inconnue.");
                        Console.ReadKey();  // Pause pour que l'utilisateur puisse lire le message
                        start();  // Redémarrer le menu
                        break;
                }
            }
        }
    }
}

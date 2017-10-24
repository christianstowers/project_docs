//
//  ViewController.swift
//  My Pokemon
//
//  Created by Christian on 10/9/17.
//  Copyright © 2017 Christian. All rights reserved.
//

import UIKit
import AVFoundation

class ViewController: UIViewController {

    @IBOutlet weak var tbPokemonName: UITextField!
    @IBOutlet weak var imgPokemon: UIImageView!
    @IBOutlet weak var lbPokemonName: UILabel!
    
    var pokemonList: [String] = ["caterpie", "pikachu", "ekans", "clefairy"]
    var player: AVAudioPlayer!
    //normally xcode would have you initialize AVAudioPLayer here, i.e. 
    //AVAudioPlayer = AVAudioPlayer(), but I want to initialize it later as 
    //a condition to my searches, so the intialization will be inside the
    //@IBAction func bSearch. the "!" tells xcode not worry, that I'll be 
    //intializing this later in the program.
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func bSearch(sender: AnyObject) {
        lbPokemonName.text = ""
        let pokemonName = tbPokemonName.text
        var isFound = false
        
        if pokemonName != "" {
            for name in pokemonList {
                if pokemonName == name {
                    lbPokemonName.text = pokemonName
                    showPokemon(name)
                    //playSound("found")
                    isFound = true
                    break
                }
            }
            
            if !isFound {
                lbPokemonName.text = "Can't find \(pokemonName!)"
                showPokemon("")
                //playSound("not_found")
            }
            
        } else {
            //will display an error message
            let alert = UIAlertController(title: "Alert",
                message: "There are as yet no nameless pokemon. Try again.",
                preferredStyle: UIAlertControllerStyle.Alert)
            let action = UIAlertAction(title: "OK",
                style: UIAlertActionStyle.Default,
                handler: nil)
            alert.addAction(action)
            self.presentViewController(alert, animated: true, completion: nil)
        }
    
    }

    func showPokemon(_ name: String) {
        imgPokemon.image = UIImage(named: name)
    }
//   this doesn't work currently(10/11 18:14). error at Bundle and URL
//   https://forums.developer.apple.com/thread/86395 offers two solutions.
//   try 'em out.
    
//    func playSound(_ sound: String) {
//        let audioPath = Bundle.main.path(forResource: sound, ofType: "wav")!
//        
//        do {
//            try player = AVAudioPlayer(contentsOf: URL(fileURLWithPath: audioPath)))
//            player.play()
//        }
//        catch{
//            print("Can't find the audio file.")
//        }
//        
//    }
    
    
    
    
    
    
    
}


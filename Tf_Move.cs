using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.Robotics.ROSTCPConnector;
using TFMessageMsg = RosMessageTypes.Tf2.TFMessageMsg;

public class Tf_Move : MonoBehaviour
{
    ROSConnection ros;
    public string frame_id;
    public float translation_x;
    public float translation_y;
    public float rotation_z;
    public float rotation_w;

    // Start is called before the first frame update
    void Start()
    {
        ros = ROSConnection.GetOrCreateInstance();
        ros.Subscribe<TFMessageMsg>("tf", OnSubscribe); 
    }

    // Update is called once per frame
    void Update()
    {
        gameObject.transform.position = new Vector3(translation_x, 0, translation_y);
        gameObject.transform.rotation = new Quaternion(0, rotation_z, 0, rotation_w);
    }

    void OnSubscribe(TFMessageMsg msg)
    {
        frame_id = msg.transforms[0].header.frame_id;
        if (frame_id=="map"){
            translation_x = Mathf.Floor((float)msg.transforms[1].transform.translation.x*100) / 100 ;
            translation_y = Mathf.Floor((float)msg.transforms[1].transform.translation.y*100) / 100 ;
            rotation_z = Mathf.Floor((float)msg.transforms[1].transform.rotation.z*100) / 100 * -1;
            rotation_w = Mathf.Floor((float)msg.transforms[1].transform.rotation.w*100) / 100;
            Debug.Log("Subscribe : " + translation_x + "," + translation_y + "," + rotation_z + "," + rotation_w);
        }
        
    }
}

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
        gameObject.transform.position = new Vector3(translation_y, 0.1f, translation_x);
        gameObject.transform.rotation = new Quaternion(0, rotation_z, 0, rotation_w);
    }

    void OnSubscribe(TFMessageMsg msg)
    {
        frame_id = msg.transforms[0].header.frame_id;
        if (frame_id=="map"){
            translation_x = (float)msg.transforms[1].transform.translation.x;
            translation_y = (float)msg.transforms[1].transform.translation.y * -1;
            rotation_z = (float)msg.transforms[1].transform.rotation.z * -1;
            rotation_w = (float)msg.transforms[1].transform.rotation.w;
        }
        
    }
}
